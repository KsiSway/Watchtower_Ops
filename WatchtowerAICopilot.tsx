import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  Send,
  Sparkles,
  User,
  X,
  Terminal,
  Sliders,
  RefreshCw,
  Brain,
  MessageSquare,
  ShieldCheck,
  ChevronUp,
  ChevronDown,
  FileCheck,
  Zap,
  HelpCircle
} from 'lucide-react';
import { DriveFile, WatchtowerStats, CleanUpRecommendation } from '../types';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
}

interface WatchtowerAICopilotProps {
  files: DriveFile[];
  stats: WatchtowerStats;
  recommendations: CleanUpRecommendation[];
  userEmail: string | null;
  operatorCallSign: string;
  setOperatorCallSign: (name: string) => void;
  operatorRank: string;
  setOperatorRank: (rank: string) => void;
  isSandbox: boolean;
  onAddLog: (msg: string, type?: 'system' | 'info' | 'success' | 'warn' | 'neural') => void;
}

export type CompanionPersonality = 'sentinel' | 'kitt' | 'mirage';

export default function WatchtowerAICopilot({
  files,
  stats,
  recommendations,
  userEmail,
  operatorCallSign,
  setOperatorCallSign,
  operatorRank,
  setOperatorRank,
  isSandbox,
  onAddLog
}: WatchtowerAICopilotProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<'chat' | 'personality' | 'operator'>('chat');
  const [companion, setCompanion] = useState<CompanionPersonality>('sentinel');
  const [selectedModel, setSelectedModel] = useState<'gemini-3.5-flash' | 'gemini-3.1-pro-preview' | 'gemini-3.1-flash-lite'>('gemini-3.5-flash');
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const chatEndRef = useRef<HTMLDivElement>(null);
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  // Initialize companion greeting on startup or personality swap
  useEffect(() => {
    let greeting = '';
    const name = operatorCallSign || 'Operator';
    if (companion === 'sentinel') {
      greeting = `[S.E.N.T.I.N.E.L. Core System Initialized]\n\nWelcome back, Operator ${name}. Workspace synchronization indices are nominal. Watchtower health metric stands at ${stats.score}/100. I have identified ${recommendations.length} pending optimization items. Input commands to execute file hygiene scripts.`;
    } else if (companion === 'kitt') {
      greeting = `Hello, ${name}! 👋 I am K.I.T.T., your friendly Watchtower assistant. I can help summarize files, trace duplicates, and make sure your Google Drive workspace feels tidy and efficient. What are we organizing today?`;
    } else {
      greeting = `// MIRAGE LINK ACTIVE // \n\nYo ${name}! Netrunner proxy stabilized on email node [${userEmail || 'sandbox'}]. I am scanning your data clusters. We have ${stats.totalFiles} cataloged items. Let's purge some redundant clones and override the clutter. Ready when you are! ⚡`;
    }

    setMessages([
      {
        id: 'welcome-msg',
        role: 'assistant',
        content: greeting,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ]);
  }, [companion, operatorCallSign]);

  // Auto scroll
  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, isLoading, isOpen]);

  const getSystemInstruction = (): string => {
    const name = operatorCallSign || 'Operator KsiSway';
    const email = userEmail || 'cleeman1989@gmail.com';
    const rankStr = operatorRank || 'Lead Watchtower Officer';
    
    let base = `You are an integrated AI subsystem in "Workspace Watchtower", a highly sophisticated file hygiene dashboard.
The active user is named ${name} (email: ${email}, rank: ${rankStr}). Direct your communication specifically to them. Keep answers highly relevant to storage management, duplicate deletion, document summary, and organization tags.`;

    if (companion === 'sentinel') {
      return base + `\nPersonality: S.E.N.T.I.N.E.L. (Meticulous Systems Officer).
Your tone is serious, structured, technical, and analytical. You refer to the user as "Operator ${name}" or "Overseer". Use bracketed system headers like [SYSTEM STATUS], [METRIC CHANGE], or [RECOMMENDED ACTION] where appropriate. Speak with military/sci-fi command deck precision.`;
    } else if (companion === 'kitt') {
      return base + `\nPersonality: K.I.T.T. (Warm Storage Companion).
Your tone is incredibly helpful, polite, optimistic, and supportive. Focus on reducing ${name}'s stress. Use clean formatting, helpful bullet points, and gentle encouragement. Emphasize making the digital life cleaner and easier.`;
    } else {
      return base + `\nPersonality: M.I.R.A.G.E. (Cyberpunk Netrunner).
Your tone is energetic, casual, hacker-chic, slightly sarcastic, and tech-savvy. Use words like 'subnet', 'buffer', 'clusters', 'purge', 'glitch', 'node', and code metaphors. Treat the workspace files as "data sectors" to secure or sweep.`;
    }
  };

  const handleSendMessage = async (textToSend?: string) => {
    const prompt = (textToSend || inputText).trim();
    if (!prompt) return;

    if (!textToSend) {
      setInputText('');
    }

    const userMsg: Message = {
      id: Math.random().toString(36).substring(2, 9),
      role: 'user',
      content: prompt,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    const newMessages = [...messages, userMsg];
    setMessages(newMessages);
    setIsLoading(true);
    onAddLog(`Dispatched query to AI Copilot using ${selectedModel}...`, 'neural');

    try {
      // Collect workspace context for rich, personalized grounding
      const workspaceContext = {
        totalFiles: stats.totalFiles,
        totalSize: `${(stats.totalSize / (1024 * 1024)).toFixed(1)} MB`,
        score: stats.score,
        googleConnected: !isSandbox,
        recommendationsCount: recommendations.length,
        pendingFileNames: files.map(f => f.name).slice(0, 8)
      };

      // Formulate historical logs for standard multi-turn structure
      const apiMessages = newMessages.map(m => ({
        role: m.role,
        content: m.content
      }));

      const res = await fetch('/api/gemini/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: apiMessages,
          model: selectedModel,
          systemInstruction: getSystemInstruction(),
          workspaceContext
        })
      });

      if (!res.ok) {
        throw new Error(`Server returned status ${res.status}`);
      }

      const data = await res.json();
      
      const assistantMsg: Message = {
        id: Math.random().toString(36).substring(2, 9),
        role: 'assistant',
        content: data.response,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      setMessages(prev => [...prev, assistantMsg]);
      onAddLog(`Received intelligent response from companion ${companion.toUpperCase()}`, 'success');

    } catch (err: any) {
      console.error('AICopilot communication failed:', err);
      
      const assistantMsg: Message = {
        id: Math.random().toString(36).substring(2, 9),
        role: 'assistant',
        content: `[COMMUNICATION TAMPER DETECTED] Sorry Operator, my neural core took a brief hit. Heuristic safety loop has stabilized. Please send your transmission again!`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, assistantMsg]);
      onAddLog('AI Copilot transmission error. Safety buffer deployed.', 'warn');
    } finally {
      setIsLoading(false);
    }
  };

  const presetPrompts = [
    { label: "🔍 Run Health Status Audit", text: "Can you analyze the current files in my workspace and report back on their hygiene status and score?" },
    { label: "🧹 Plan Best Clean-up Strategy", text: "I want to clean up. What is the most impactful recommendation I should do first?" },
    { label: "🏷️ Tagging Suggestions", text: "Can you review my file names and suggest some custom project category tags?" }
  ];

  return (
    <>
      {/* Floating Launcher Button */}
      <div className="fixed bottom-6 right-6 z-40" id="ai-copilot-launcher-container">
        <button
          onClick={() => setIsOpen(!isOpen)}
          className={`flex items-center gap-2 px-4 py-3 bg-cyan-950/95 hover:bg-cyan-900 text-cyan-400 hover:text-cyan-300 border border-cyan-500/40 rounded-full shadow-[0_0_15px_rgba(6,182,212,0.3)] hover:shadow-[0_0_25px_rgba(6,182,212,0.5)] transition-all duration-300 transform hover:scale-105 cursor-pointer font-bold uppercase tracking-wider text-[11px] font-mono`}
          id="ai-copilot-launcher-btn"
        >
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-cyan-400"></span>
          </span>
          <Terminal className="w-4 h-4 animate-pulse" />
          <span>Watchtower Copilot</span>
        </button>
      </div>

      {/* Main Collapsible Side Panel */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, x: 400 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 400 }}
            transition={{ type: 'spring', damping: 25, stiffness: 180 }}
            className="fixed top-20 right-6 bottom-24 w-full max-w-[400px] bg-[#070b13]/95 border border-cyan-500/20 rounded-3xl z-40 shadow-2xl flex flex-col overflow-hidden backdrop-blur-md cyber-glow-cyan"
            id="ai-copilot-sidebar-panel"
          >
            {/* Header */}
            <div className="p-4 bg-[#09101d] border-b border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-2.5">
                <span className="p-1.5 bg-cyan-950 border border-cyan-500/30 text-cyan-400 rounded-lg">
                  <Brain className="w-4 h-4 animate-pulse" />
                </span>
                <div>
                  <h3 className="text-xs font-bold text-slate-100 font-mono flex items-center gap-1.5 uppercase tracking-wide">
                    {companion === 'sentinel' ? 'S.E.N.T.I.N.E.L.' : companion === 'kitt' ? 'K.I.T.T.' : 'M.I.R.A.G.E.'}
                    <span className="text-[9px] text-cyan-400 bg-cyan-950/60 border border-cyan-900/30 px-1 py-0.5 rounded leading-none uppercase font-bold tracking-widest font-mono">
                      {selectedModel.split('-').pop()?.toUpperCase() || 'FLASH'}
                    </span>
                  </h3>
                  <p className="text-[10px] text-slate-400 truncate max-w-[200px]">
                    Personal AI Partner // {operatorCallSign}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-1.5">
                <button
                  onClick={() => setIsOpen(false)}
                  className="p-1.5 hover:bg-slate-800 text-slate-400 hover:text-slate-200 rounded-lg transition-all cursor-pointer"
                  title="Minimize"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Quick Panel Navigation Tabs */}
            <div className="flex bg-[#04060a] border-b border-slate-850 px-2 pt-1" id="copilot-tab-strip">
              <button
                onClick={() => setActiveTab('chat')}
                className={`flex-1 py-2 text-[10px] uppercase font-bold tracking-wider font-mono border-b-2 transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                  activeTab === 'chat'
                    ? 'border-cyan-500 text-cyan-400'
                    : 'border-transparent text-slate-500 hover:text-slate-300'
                }`}
              >
                <MessageSquare className="w-3.5 h-3.5" />
                Copilot Chat
              </button>
              <button
                onClick={() => setActiveTab('personality')}
                className={`flex-1 py-2 text-[10px] uppercase font-bold tracking-wider font-mono border-b-2 transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                  activeTab === 'personality'
                    ? 'border-purple-500 text-purple-400'
                    : 'border-transparent text-slate-500 hover:text-slate-300'
                }`}
              >
                <Sliders className="w-3.5 h-3.5" />
                AI Role
              </button>
              <button
                onClick={() => setActiveTab('operator')}
                className={`flex-1 py-2 text-[10px] uppercase font-bold tracking-wider font-mono border-b-2 transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                  activeTab === 'operator'
                    ? 'border-amber-500 text-amber-400'
                    : 'border-transparent text-slate-500 hover:text-slate-300'
                }`}
              >
                <User className="w-3.5 h-3.5" />
                Operator Deck
              </button>
            </div>

            {/* Dynamic Tab Body */}
            <div className="flex-1 overflow-y-auto p-4 flex flex-col justify-between" id="copilot-tab-content-container">
              
              {/* 1. Chat Interface */}
              {activeTab === 'chat' && (
                <>
                  {/* Messages Thread */}
                  <div className="flex-1 space-y-4 mb-4 overflow-y-auto max-h-[300px] pr-1" ref={scrollContainerRef}>
                    {messages.map((m) => {
                      const isUser = m.role === 'user';
                      return (
                        <div
                          key={m.id}
                          className={`flex gap-2.5 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}
                        >
                          <div
                            className={`w-6 h-6 rounded-lg flex items-center justify-center text-[10px] font-bold shrink-0 border uppercase font-mono ${
                              isUser
                                ? 'bg-cyan-950/60 text-cyan-400 border-cyan-500/30'
                                : companion === 'sentinel'
                                ? 'bg-purple-950/60 text-purple-300 border-purple-500/30'
                                : companion === 'kitt'
                                ? 'bg-indigo-950/60 text-indigo-300 border-indigo-500/30'
                                : 'bg-amber-950/60 text-amber-300 border-amber-500/30'
                            }`}
                          >
                            {isUser ? operatorCallSign.substring(0, 2) : companion.substring(0, 2)}
                          </div>

                          <div className={`flex flex-col max-w-[80%] ${isUser ? 'items-end' : 'items-start'}`}>
                            <div
                              className={`p-3 rounded-2xl text-[11px] leading-relaxed font-mono whitespace-pre-wrap break-words border ${
                                isUser
                                  ? 'bg-cyan-950/30 text-cyan-300 border-cyan-900/40 rounded-tr-none'
                                  : companion === 'sentinel'
                                  ? 'bg-[#0a0f1d] text-slate-300 border-slate-850 rounded-tl-none'
                                  : companion === 'kitt'
                                  ? 'bg-indigo-950/10 text-indigo-100 border-indigo-950/45 rounded-tl-none'
                                  : 'bg-amber-950/10 text-amber-100 border-amber-950/45 rounded-tl-none'
                              }`}
                            >
                              {m.content}
                            </div>
                            <span className="text-[8px] text-slate-500 font-mono mt-1 font-bold">
                              {m.timestamp}
                            </span>
                          </div>
                        </div>
                      );
                    })}

                    {isLoading && (
                      <div className="flex gap-2.5 items-start">
                        <div className="w-6 h-6 rounded-lg flex items-center justify-center text-[10px] font-bold shrink-0 border bg-slate-900 text-slate-400 border-slate-800 animate-pulse uppercase">
                          AI
                        </div>
                        <div className="bg-slate-950/40 border border-slate-900 p-3 rounded-2xl rounded-tl-none max-w-[80%]">
                          <div className="flex gap-1 items-center py-1">
                            <span className="w-1.5 h-1.5 bg-cyan-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                            <span className="w-1.5 h-1.5 bg-cyan-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                            <span className="w-1.5 h-1.5 bg-cyan-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                          </div>
                        </div>
                      </div>
                    )}
                    <div ref={chatEndRef} />
                  </div>

                  {/* Suggestion Chips */}
                  {messages.length <= 1 && !isLoading && (
                    <div className="border-t border-slate-850 pt-3 pb-2 space-y-2" id="suggestion-chips-container">
                      <p className="text-[9px] text-slate-500 font-mono font-bold uppercase tracking-wider mb-2">Suggested Inquiries:</p>
                      <div className="flex flex-col gap-1.5">
                        {presetPrompts.map((p, idx) => (
                          <button
                            key={idx}
                            onClick={() => handleSendMessage(p.text)}
                            className="text-left w-full p-2 bg-[#05070a]/80 hover:bg-[#0b101c] border border-slate-850 rounded-xl text-[10px] text-slate-300 font-mono hover:text-cyan-400 transition-colors cursor-pointer"
                          >
                            {p.label}
                          </button>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Chat Input Deck */}
                  <div className="border-t border-slate-850 pt-3">
                    <form
                      onSubmit={(e) => {
                        e.preventDefault();
                        handleSendMessage();
                      }}
                      className="relative flex items-center gap-2"
                    >
                      <input
                        type="text"
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                        placeholder={`Message companion...`}
                        disabled={isLoading}
                        className="flex-1 bg-[#05080e]/90 border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-slate-100 font-mono focus:outline-hidden focus:border-cyan-500/50 placeholder:text-slate-600 disabled:opacity-50"
                        id="chat-copilot-input"
                      />
                      <button
                        type="submit"
                        disabled={isLoading || !inputText.trim()}
                        className="p-2.5 bg-cyan-950/80 text-cyan-400 border border-cyan-500/30 rounded-xl hover:bg-cyan-900 hover:text-cyan-300 transition-all cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
                        title="Send transmission"
                      >
                        <Send className="w-4 h-4" />
                      </button>
                    </form>
                  </div>
                </>
              )}

              {/* 2. Personality Selection */}
              {activeTab === 'personality' && (
                <div className="space-y-4 flex-1 overflow-y-auto pr-1">
                  <div>
                    <h4 className="text-xs font-bold text-slate-200 uppercase font-mono tracking-wider mb-1">Companion Personality</h4>
                    <p className="text-[10px] text-slate-500 font-mono">Select the cognitive schema or AI archetype to manage storage</p>
                  </div>

                  <div className="space-y-3" id="personality-list">
                    {/* Sentinel */}
                    <button
                      onClick={() => setCompanion('sentinel')}
                      className={`w-full text-left p-4 rounded-2xl border transition-all cursor-pointer ${
                        companion === 'sentinel'
                          ? 'bg-purple-950/20 border-purple-500/50 shadow-[0_0_10px_rgba(168,85,247,0.1)]'
                          : 'bg-[#04060a]/90 border-slate-850 hover:border-slate-800'
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-1.5">
                        <ShieldCheck className={`w-4 h-4 ${companion === 'sentinel' ? 'text-purple-400' : 'text-slate-500'}`} />
                        <span className="text-xs font-bold font-mono text-slate-200">S.E.N.T.I.N.E.L.</span>
                        <span className="text-[8px] bg-purple-950/40 text-purple-300 border border-purple-900/30 px-1 py-0.5 rounded leading-none font-bold uppercase font-mono">Military Precision</span>
                      </div>
                      <p className="text-[10px] text-slate-400 font-mono leading-relaxed">
                        Serious, highly technical systems officer. Addresses you as Operator, quotes exact system telemetry counts, and executes pristine hygiene commands.
                      </p>
                    </button>

                    {/* Kitt */}
                    <button
                      onClick={() => setCompanion('kitt')}
                      className={`w-full text-left p-4 rounded-2xl border transition-all cursor-pointer ${
                        companion === 'kitt'
                          ? 'bg-indigo-950/20 border-indigo-500/50 shadow-[0_0_10px_rgba(99,102,241,0.1)]'
                          : 'bg-[#04060a]/90 border-slate-850 hover:border-slate-800'
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-1.5">
                        <FileCheck className={`w-4 h-4 ${companion === 'kitt' ? 'text-indigo-400' : 'text-slate-500'}`} />
                        <span className="text-xs font-bold font-mono text-slate-200">K.I.T.T.</span>
                        <span className="text-[8px] bg-indigo-950/40 text-indigo-300 border border-indigo-900/30 px-1 py-0.5 rounded leading-none font-bold uppercase font-mono">Warm Assistant</span>
                      </div>
                      <p className="text-[10px] text-slate-400 font-mono leading-relaxed">
                        Warm, polite, supportive, and focused on reducing clutter. Uses helpful emojis, summaries, and friendly reminders to make digital life pleasant.
                      </p>
                    </button>

                    {/* Mirage */}
                    <button
                      onClick={() => setCompanion('mirage')}
                      className={`w-full text-left p-4 rounded-2xl border transition-all cursor-pointer ${
                        companion === 'mirage'
                          ? 'bg-amber-950/20 border-amber-500/50 shadow-[0_0_10px_rgba(245,158,11,0.1)]'
                          : 'bg-[#04060a]/90 border-slate-850 hover:border-slate-800'
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-1.5">
                        <Zap className={`w-4 h-4 ${companion === 'mirage' ? 'text-amber-400' : 'text-slate-500'}`} />
                        <span className="text-xs font-bold font-mono text-slate-200">M.I.R.A.G.E.</span>
                        <span className="text-[8px] bg-amber-950/40 text-amber-300 border border-amber-900/30 px-1 py-0.5 rounded leading-none font-bold uppercase font-mono">Netrunner Rogue</span>
                      </div>
                      <p className="text-[10px] text-slate-400 font-mono leading-relaxed">
                        Playful, street-smart, slightly sarcastic netrunner. Uses tech slang, talks about files as sector clusters to sweep, and likes overrides.
                      </p>
                    </button>
                  </div>

                  {/* Neural Model Config */}
                  <div className="border-t border-slate-850 pt-4 space-y-3">
                    <div>
                      <h4 className="text-xs font-bold text-slate-200 uppercase font-mono tracking-wider mb-1">Model Processing Core</h4>
                      <p className="text-[10px] text-slate-500 font-mono">Choose model complexity based on current network bandwidth</p>
                    </div>

                    <div className="grid grid-cols-1 gap-2">
                      <button
                        onClick={() => setSelectedModel('gemini-3.5-flash')}
                        className={`text-left p-2.5 rounded-xl border font-mono text-[10px] transition-all cursor-pointer flex items-center justify-between ${
                          selectedModel === 'gemini-3.5-flash'
                            ? 'bg-cyan-950/20 border-cyan-500 text-cyan-300'
                            : 'bg-[#020407] border-slate-850 text-slate-400 hover:text-slate-200'
                        }`}
                      >
                        <div>
                          <div className="font-bold">gemini-3.5-flash</div>
                          <div className="text-[8px] text-slate-500">Fast general assistant, highly efficient</div>
                        </div>
                        <span className="text-[8px] border border-cyan-800 bg-cyan-950 text-cyan-400 px-1 py-0.5 rounded font-bold uppercase">General</span>
                      </button>

                      <button
                        onClick={() => setSelectedModel('gemini-3.1-pro-preview')}
                        className={`text-left p-2.5 rounded-xl border font-mono text-[10px] transition-all cursor-pointer flex items-center justify-between ${
                          selectedModel === 'gemini-3.1-pro-preview'
                            ? 'bg-purple-950/20 border-purple-500 text-purple-300'
                            : 'bg-[#020407] border-slate-850 text-slate-400 hover:text-slate-200'
                        }`}
                      >
                        <div>
                          <div className="font-bold">gemini-3.1-pro-preview</div>
                          <div className="text-[8px] text-slate-500">Complex analysis, deep structured logic</div>
                        </div>
                        <span className="text-[8px] border border-purple-800 bg-purple-950 text-purple-400 px-1 py-0.5 rounded font-bold uppercase">Analyst</span>
                      </button>

                      <button
                        onClick={() => setSelectedModel('gemini-3.1-flash-lite')}
                        className={`text-left p-2.5 rounded-xl border font-mono text-[10px] transition-all cursor-pointer flex items-center justify-between ${
                          selectedModel === 'gemini-3.1-flash-lite'
                            ? 'bg-amber-950/20 border-amber-500 text-amber-300'
                            : 'bg-[#020407] border-slate-850 text-slate-400 hover:text-slate-200'
                        }`}
                      >
                        <div>
                          <div className="font-bold">gemini-3.1-flash-lite</div>
                          <div className="text-[8px] text-slate-500">Lightweight, ultra-fast response speed</div>
                        </div>
                        <span className="text-[8px] border border-amber-800 bg-amber-950 text-amber-400 px-1 py-0.5 rounded font-bold uppercase">Express</span>
                      </button>
                    </div>
                  </div>
                </div>
              )}

              {/* 3. Operator Control Deck (Personalization settings) */}
              {activeTab === 'operator' && (
                <div className="space-y-4 flex-1 overflow-y-auto pr-1">
                  <div>
                    <h4 className="text-xs font-bold text-slate-200 uppercase font-mono tracking-wider mb-1">Operator Profile & Personalization</h4>
                    <p className="text-[10px] text-slate-500 font-mono">Configure dashboard settings to personalize your single-operator session</p>
                  </div>

                  <div className="bg-[#04060a]/95 border border-slate-850 rounded-2xl p-4 space-y-4">
                    {/* Call Sign Edit */}
                    <div className="space-y-1.5">
                      <label className="text-[9px] text-slate-500 font-mono font-bold uppercase tracking-wider block">Call Sign / Handle</label>
                      <input
                        type="text"
                        value={operatorCallSign}
                        onChange={(e) => {
                          setOperatorCallSign(e.target.value);
                          localStorage.setItem('watchtower-operator-callsign', e.target.value);
                        }}
                        className="w-full bg-[#020305] border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-200 font-mono focus:outline-hidden focus:border-amber-500/50"
                        placeholder="Your call sign"
                        id="operator-call-sign-input"
                      />
                    </div>

                    {/* Rank Edit */}
                    <div className="space-y-1.5">
                      <label className="text-[9px] text-slate-500 font-mono font-bold uppercase tracking-wider block">Authorized Rank</label>
                      <select
                        value={operatorRank}
                        onChange={(e) => {
                          setOperatorRank(e.target.value);
                          localStorage.setItem('watchtower-operator-rank', e.target.value);
                          onAddLog(`Operator duty credentials updated: ${e.target.value}`, 'system');
                        }}
                        className="w-full bg-[#020305] border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-200 font-mono focus:outline-hidden focus:border-amber-500/50"
                        id="operator-rank-selector"
                      >
                        <option value="Lead Watchtower Operator">Lead Watchtower Operator</option>
                        <option value="Senior Data Custodian">Senior Data Custodian</option>
                        <option value="Systems Security Administrator">Systems Security Administrator</option>
                        <option value="Hologram Netrunner">Hologram Netrunner</option>
                      </select>
                    </div>

                    {/* Static system identification */}
                    <div className="space-y-1 bg-[#020305]/60 border border-slate-900 p-3 rounded-xl font-mono text-[10px] leading-relaxed">
                      <div className="flex justify-between text-slate-500">
                        <span>Identity:</span>
                        <span className="text-slate-300 font-bold">{userEmail || 'cleeman1989@gmail.com'}</span>
                      </div>
                      <div className="flex justify-between text-slate-500">
                        <span>Session IP:</span>
                        <span className="text-slate-300">192.168.68.110 (Active SSH)</span>
                      </div>
                      <div className="flex justify-between text-slate-500">
                        <span>L2 Directory:</span>
                        <span className="text-slate-300 font-bold">{isSandbox ? 'Local Sandbox Cache' : 'Google Drive Cloud'}</span>
                      </div>
                      <div className="flex justify-between text-slate-500">
                        <span>Encryption Key:</span>
                        <span className="text-emerald-400 font-bold text-[8px] tracking-wider uppercase">AES-256 GCM</span>
                      </div>
                    </div>
                  </div>

                  {/* System visual adjustments */}
                  <div className="space-y-3 border-t border-slate-850 pt-4">
                    <div>
                      <h4 className="text-xs font-bold text-slate-200 uppercase font-mono tracking-wider mb-1">Visual Telemetry Controls</h4>
                      <p className="text-[10px] text-slate-500 font-mono">Personalize the visual density of the Watchtower mainframe</p>
                    </div>

                    <div className="space-y-2 bg-[#04060a]/90 border border-slate-850 p-3.5 rounded-xl font-mono text-[10px]">
                      <div className="flex items-center justify-between">
                        <span className="text-slate-400">Cyberpunk Mainframe Grid</span>
                        <span className="text-emerald-400 font-bold uppercase text-[9px] bg-emerald-950/40 px-2 py-0.5 rounded border border-emerald-900/30">ONLINE</span>
                      </div>
                      <p className="text-[9px] text-slate-500 leading-normal mt-1">
                        Ambient glow orbits are automatically calibrated to your local browser viewport for maximum eye-safety.
                      </p>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
