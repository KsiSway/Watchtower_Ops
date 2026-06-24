import React, { useEffect, useState, useRef } from 'react';
import { Terminal, Trash2, Pause, Play, Activity, Download } from 'lucide-react';
import { LogEntry } from '../types';

interface SystemActivityLogProps {
  logs: LogEntry[];
  onClear: () => void;
}

export default function SystemActivityLog({ logs, onClear }: SystemActivityLogProps) {
  const [isPaused, setIsPaused] = useState(false);
  const [filterMode, setFilterMode] = useState<'all' | 'diagnose'>('all');
  const [displayedLogs, setDisplayedLogs] = useState<LogEntry[]>(logs);
  const scrollerRef = useRef<HTMLDivElement>(null);

  // Update displayed logs if not paused
  useEffect(() => {
    if (!isPaused) {
      setDisplayedLogs(logs);
    }
  }, [logs, isPaused]);

  // Compute filtered logs
  const filteredLogs = displayedLogs.filter((log) => {
    if (filterMode === 'all') return true;
    if (filterMode === 'diagnose') {
      const isWarningOrError = log.type === 'warn' || log.type === 'error';
      const isConflict = log.message.toLowerCase().includes('conflict');
      return isWarningOrError || isConflict;
    }
    return true;
  });

  // Auto-scroll to the bottom of the log container when filteredLogs update
  useEffect(() => {
    if (scrollerRef.current) {
      scrollerRef.current.scrollTo({
        top: scrollerRef.current.scrollHeight,
        behavior: 'smooth'
      });
    }
  }, [filteredLogs]);

  const downloadLogs = () => {
    if (displayedLogs.length === 0) return;
    
    const textContent = displayedLogs
      .map((log) => `[${log.timestamp}] ${getLogPrefix(log.type)}: ${log.message}`)
      .join('\n');

    const blob = new Blob([textContent], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `watchtower-system-activity-${new Date().toISOString().split('T')[0]}.log`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const getLogColorClass = (type: LogEntry['type']) => {
    switch (type) {
      case 'success':
        return 'text-emerald-400';
      case 'warn':
        return 'text-amber-400';
      case 'error':
        return 'text-rose-500 font-bold';
      case 'neural':
        return 'text-fuchsia-400';
      case 'system':
        return 'text-sky-400';
      case 'info':
      default:
        return 'text-cyan-400/80';
    }
  };

  const getLogPrefix = (type: LogEntry['type']) => {
    switch (type) {
      case 'success':
        return '[ OK ]';
      case 'warn':
        return '[WARN]';
      case 'error':
        return '[FAIL]';
      case 'neural':
        return '[AI_3.5]';
      case 'system':
        return '[SYS]';
      case 'info':
      default:
        return '[INFO]';
    }
  };

  return (
    <div 
      className="bg-[#090d16]/80 border border-cyan-500/20 rounded-3xl p-4 sm:p-5 relative backdrop-blur-md shadow-[0_0_15px_rgba(6,182,212,0.05)]"
      id="system-activity-panel"
    >
      {/* Header Controls */}
      <div className="flex items-center justify-between border-b border-slate-800/60 pb-3 mb-3">
        <div className="flex items-center gap-2">
          <span className="relative flex h-2 w-2">
            <span className={`animate-ping absolute inline-flex h-full w-full rounded-full opacity-75 ${isPaused ? 'bg-amber-400' : 'bg-cyan-400'}`}></span>
            <span className={`relative inline-flex rounded-full h-2 w-2 ${isPaused ? 'bg-amber-500' : 'bg-cyan-500'}`}></span>
          </span>
          <h4 className="text-xs font-bold uppercase tracking-widest text-slate-100 flex items-center gap-1.5 font-mono">
            <Terminal className="w-3.5 h-3.5 text-cyan-400" />
            Watchtower System Activity Ticker
          </h4>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setIsPaused(!isPaused)}
            className={`flex items-center gap-1 px-2.5 py-1 rounded-lg text-[10px] uppercase font-bold tracking-wider font-mono border transition-all ${
              isPaused 
                ? 'bg-amber-950/20 border-amber-500/30 text-amber-400 hover:bg-amber-950/40' 
                : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200 hover:bg-slate-800'
            }`}
            title={isPaused ? 'Resume live ticker feed' : 'Pause live ticker feed'}
          >
            {isPaused ? (
              <>
                <Play className="w-3 h-3 text-emerald-400" />
                Resume
              </>
            ) : (
              <>
                <Pause className="w-3 h-3 text-amber-400" />
                Pause
              </>
            )}
          </button>
          
          <button
            onClick={downloadLogs}
            disabled={displayedLogs.length === 0}
            className="flex items-center gap-1 px-2.5 py-1 bg-slate-900 border border-slate-800 hover:border-cyan-500/30 hover:bg-cyan-950/15 hover:text-cyan-400 text-slate-400 rounded-lg text-[10px] uppercase font-bold tracking-wider font-mono transition-all disabled:opacity-40 disabled:pointer-events-none cursor-pointer"
            title="Download visible logs as .log file"
            id="download-logs-btn"
          >
            <Download className="w-3 h-3" />
            Download
          </button>

          <button
            onClick={onClear}
            className="flex items-center gap-1 px-2.5 py-1 bg-slate-900 border border-slate-800 hover:border-rose-950 hover:bg-rose-950/15 hover:text-rose-400 text-slate-400 rounded-lg text-[10px] uppercase font-bold tracking-wider font-mono transition-all cursor-pointer"
            title="Flush memory logs"
            id="flush-logs-btn"
          >
            <Trash2 className="w-3 h-3" />
            Flush
          </button>
        </div>
      </div>

      {/* Diagnostics Filters Row */}
      <div className="flex flex-wrap items-center justify-between gap-2.5 mb-3 px-1" id="log-diagnostics-filter-bar">
        <div className="flex items-center gap-1.5 bg-[#04060a]/90 border border-slate-850 p-1 rounded-xl">
          <button
            onClick={() => setFilterMode('all')}
            className={`px-3 py-1.5 rounded-lg text-[9px] font-mono uppercase tracking-wider font-bold transition-all cursor-pointer ${
              filterMode === 'all'
                ? 'bg-cyan-500/10 text-cyan-400 border border-cyan-500/20'
                : 'text-slate-500 hover:text-slate-300 border border-transparent'
            }`}
          >
            All Logs ({displayedLogs.length})
          </button>
          <button
            onClick={() => setFilterMode('diagnose')}
            className={`px-3 py-1.5 rounded-lg text-[9px] font-mono uppercase tracking-wider font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
              filterMode === 'diagnose'
                ? 'bg-amber-500/10 text-amber-400 border border-amber-500/20 shadow-[0_0_8px_rgba(245,158,11,0.1)]'
                : 'text-slate-500 hover:text-slate-300 border border-transparent'
            }`}
          >
            <span className="w-1.5 h-1.5 bg-amber-400 rounded-full animate-pulse" />
            Warning & Conflicts ({displayedLogs.filter(log => log.type === 'warn' || log.type === 'error' || log.message.toLowerCase().includes('conflict')).length})
          </button>
        </div>
        
        {filterMode === 'diagnose' && (
          <span className="text-[9px] font-mono text-amber-500/90 animate-pulse bg-amber-500/5 border border-amber-500/10 px-2.5 py-1 rounded-xl">
            Diag Mode Active
          </span>
        )}
      </div>

      {/* Ticker Content */}
      <div 
        ref={scrollerRef}
        className="h-32 overflow-y-auto bg-[#05070a]/90 rounded-2xl p-3 border border-slate-900 font-mono text-[11px] leading-relaxed scrollbar-thin relative"
        id="system-terminal-log-scroller"
      >
        {displayedLogs.length === 0 ? (
          <div className="flex flex-col items-center justify-center text-center h-full text-slate-600 italic">
            <Activity className="w-5 h-5 text-slate-700 animate-pulse mb-1" />
            <span>Buffer flushed. Waiting for telemetry activities...</span>
          </div>
        ) : filteredLogs.length === 0 ? (
          <div className="flex flex-col items-center justify-center text-center h-full text-slate-500 italic py-6">
            <Activity className="w-5 h-5 text-amber-500 animate-pulse mb-1" />
            <span>No warning or sync conflict logs found in active buffer.</span>
          </div>
        ) : (
          <div className="space-y-1.5">
            {filteredLogs.map((log) => (
              <div 
                key={log.id} 
                className="flex items-start gap-2.5 hover:bg-slate-950/50 py-0.5 px-1 rounded transition-colors group"
              >
                <span className="text-[10px] text-slate-500 select-none font-medium shrink-0">
                  {log.timestamp}
                </span>
                <span className={`text-[10px] uppercase font-semibold shrink-0 select-none ${getLogColorClass(log.type)}`}>
                  {getLogPrefix(log.type)}
                </span>
                <span className="text-slate-500 select-none shrink-0 group-hover:text-cyan-500 transition-colors">▶</span>
                <span className={`break-all ${getLogColorClass(log.type)}`}>
                  {log.message}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Dynamic scan glow effect */}
      <div className="absolute bottom-0 left-10 right-10 h-px bg-gradient-to-r from-transparent via-cyan-500/10 to-transparent"></div>
    </div>
  );
}
