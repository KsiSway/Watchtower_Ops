/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { FileText, Sparkles, CheckSquare, ListTodo, AlertCircle, RefreshCw, X, Tag, Maximize2, Minimize2, Eye, ExternalLink, FileSpreadsheet, Info, Share2, Check, FileDown } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { jsPDF } from 'jspdf';
import { DriveFile, AnalysisResult } from '../types';

interface FileAnalyzerProps {
  file: DriveFile | null;
  onClose: () => void;
  isSandbox: boolean;
  onLog?: (message: string, type: 'info' | 'success' | 'warn' | 'error' | 'neural' | 'system') => void;
  onUpdateTags?: (fileId: string, tags: string[]) => void;
}

export default function FileAnalyzer({ file, onClose, isSandbox, onLog, onUpdateTags }: FileAnalyzerProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [isExpanded, setIsExpanded] = useState(false);
  const [activeTab, setActiveTab] = useState<'preview' | 'insights' | 'summary'>('preview');
  const [newTag, setNewTag] = useState('');
  const [quickViewOpen, setQuickViewOpen] = useState(false);
  const [viewerMode, setViewerMode] = useState<'dedicated' | 'iframe'>('dedicated');
  const [shareSuccess, setShareSuccess] = useState(false);
  const [aiSummary, setAiSummary] = useState<string | null>(null);
  const [aiSummaryLoading, setAiSummaryLoading] = useState(false);
  const [aiSummaryError, setAiSummaryError] = useState<string | null>(null);

  const handleShareFile = async () => {
    if (!file) return;
    const shareUrl = file.webViewLink || `https://drive.google.com/file/d/${file.id}/view`;
    const shareData = {
      title: file.name,
      text: `Check out this document: ${file.name} inspected via Watchtower AI-Sync`,
      url: shareUrl,
    };

    try {
      if (navigator.share && navigator.canShare && navigator.canShare(shareData)) {
        await navigator.share(shareData);
        if (onLog) {
          onLog(`Successfully opened system share dialog for: ${file.name}`, 'success');
        }
      } else {
        throw new Error('Web Share API not fully supported or restricted in this environment.');
      }
    } catch (err: any) {
      try {
        await navigator.clipboard.writeText(shareUrl);
        setShareSuccess(true);
        if (onLog) {
          onLog(`System sharing restricted in preview iframe. File link copied to clipboard: ${file.name}`, 'success');
        }
        setTimeout(() => setShareSuccess(false), 3000);
      } catch (clipboardErr) {
        if (onLog) {
          onLog(`Unable to share or copy file link. Link: ${shareUrl}`, 'error');
        }
      }
    }
  };

  const handleExportToPDF = () => {
    if (!file) return;

    try {
      if (onLog) {
        onLog(`Generating printable PDF document package for: ${file.name}`, 'system');
      }

      const doc = new jsPDF({ format: 'a4', unit: 'mm' });
      const leftMargin = 20;
      const rightMargin = 20;
      const contentWidth = 170;
      const pageHeightLimit = 265;
      let yPos = 25; // start offset

      // Helper for adding wrapped text
      const addWrappedText = (
        text: string,
        fontSize: number,
        isBold: boolean,
        colorHex: string = '#1e293b',
        customLineHeightFactor: number = 1.45
      ) => {
        doc.setFont('helvetica', isBold ? 'bold' : 'normal');
        doc.setFontSize(fontSize);
        
        const r = parseInt(colorHex.slice(1, 3), 16);
        const g = parseInt(colorHex.slice(3, 5), 16);
        const b = parseInt(colorHex.slice(5, 7), 16);
        doc.setTextColor(r, g, b);

        const lines = doc.splitTextToSize(text, contentWidth);
        const lineHeight = fontSize * 0.3528 * customLineHeightFactor;

        lines.forEach((line: string) => {
          if (yPos + lineHeight > pageHeightLimit) {
            doc.addPage();
            yPos = 25;
          }
          doc.text(line, leftMargin, yPos);
          yPos += lineHeight;
        });
      };

      // Helper for sections
      const addSectionHeading = (title: string, colorHex: string = '#0ea5e9') => {
        if (yPos + 18 > pageHeightLimit) {
          doc.addPage();
          yPos = 25;
        }
        
        yPos += 5;
        
        const r = parseInt(colorHex.slice(1, 3), 16);
        const g = parseInt(colorHex.slice(3, 5), 16);
        const b = parseInt(colorHex.slice(5, 7), 16);
        
        // Background fill
        doc.setFillColor(r, g, b, 0.08);
        doc.rect(leftMargin, yPos - 5, contentWidth, 8, 'F');
        
        // Accent bar
        doc.setFillColor(r, g, b);
        doc.rect(leftMargin, yPos - 5, 1.5, 8, 'F');
        
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(10.5);
        doc.setTextColor(15, 23, 42); // slate-900
        doc.text(title.toUpperCase(), leftMargin + 4, yPos + 0.8);
        
        yPos += 7;
      };

      // Helper for snippet
      const addCodeSnippetBox = (codeText: string) => {
        const lines = doc.splitTextToSize(codeText, contentWidth - 10);
        const fontSize = 8.5;
        const lineHeight = fontSize * 0.3528 * 1.4;

        doc.setFont('courier', 'normal');
        doc.setFontSize(fontSize);
        doc.setTextColor(51, 65, 85);
        
        lines.forEach((line: string) => {
          if (yPos + lineHeight > pageHeightLimit) {
            doc.addPage();
            yPos = 25;
          }
          
          doc.setFillColor(248, 250, 252);
          doc.rect(leftMargin, yPos - 3, contentWidth, lineHeight + 0.5, 'F');
          
          doc.setFillColor(203, 213, 225);
          doc.rect(leftMargin, yPos - 3, 1, lineHeight + 0.5, 'F');
          
          doc.text(line, leftMargin + 4, yPos + 0.5);
          yPos += lineHeight;
        });
        
        yPos += 4;
      };

      // --- 1. TITLE BLOCK ---
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(22);
      doc.setTextColor(15, 23, 42); // slate-900
      doc.text('Watchtower AI-Sync', leftMargin, yPos);
      yPos += 8;

      doc.setFont('helvetica', 'normal');
      doc.setFontSize(10);
      doc.setTextColor(100, 116, 139); // slate-500
      doc.text(`Intelligence analysis compilation generated on ${new Date().toLocaleDateString()}`, leftMargin, yPos);
      yPos += 12;

      // --- 2. FILE SUMMARY SECTION ---
      addSectionHeading('File Specification & Metadata', '#0ea5e9'); // Cyan
      
      // Meta Grid Table
      const metaPairs = [
        ['File Name:', file.name],
        ['File ID:', file.id],
        ['Mime Type:', file.mimeType],
        ['File Size:', file.size ? `${(file.size / 1024).toFixed(2)} KB (${file.size} bytes)` : 'Unknown'],
        ['Last Modified:', new Date(file.modifiedTime).toLocaleString()],
        ['Labels/Tags:', file.tags && file.tags.length > 0 ? file.tags.join(', ') : 'None assigned']
      ];

      doc.setFont('helvetica', 'normal');
      doc.setFontSize(9);
      metaPairs.forEach(([label, value]) => {
        if (yPos + 6 > pageHeightLimit) {
          doc.addPage();
          yPos = 25;
        }
        
        // Draw label in bold slate-700, value in normal slate-600
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(51, 65, 85);
        doc.text(label, leftMargin, yPos);
        
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(71, 85, 105);
        // Truncate value if it's too long
        const valLines = doc.splitTextToSize(value, contentWidth - 40);
        doc.text(valLines[0], leftMargin + 40, yPos);
        yPos += 6;
      });
      yPos += 4;

      // --- 3. GEMINI ANALYSIS RESULTS (if available) ---
      if (result) {
        addSectionHeading('AI Executive Summary', '#0ea5e9');
        addWrappedText(result.summary, 9.5, false, '#334155');
        yPos += 4;

        addSectionHeading(`Document Classification: ${result.projectCategory}`, '#0ea5e9');
        addWrappedText(`Confidence Mapping Score: ${result.categoryScore}% classified category strength.`, 9, false, '#475569');
        yPos += 4;

        if (result.keyTakeaways && result.keyTakeaways.length > 0) {
          addSectionHeading('Key Document Takeaways', '#10b981'); // Emerald
          result.keyTakeaways.forEach((takeaway, idx) => {
            addWrappedText(`${idx + 1}. ${takeaway}`, 9, false, '#334155');
            yPos += 2;
          });
          yPos += 4;
        }

        if (result.actionItems && result.actionItems.length > 0) {
          addSectionHeading('Extracted Action Items Checklist', '#06b6d4'); // Light blue
          result.actionItems.forEach((action, idx) => {
            addWrappedText(`[ ] ${action}`, 9, false, '#334155');
            yPos += 2;
          });
          yPos += 4;
        }
      } else {
        addSectionHeading('AI Analysis (Gemini Integration)', '#e2e8f0');
        addWrappedText('Intelligence analysis report has not been executed for this document. Run "Analyze with Gemini" in the side panel to generate structural takeaways, classifications, and interactive summary modules.', 9, true, '#64748b');
        yPos += 4;
      }

      // --- 4. CONTENT SNIPPET ---
      if (file.content) {
        addSectionHeading('Extracted Document Content Stream', '#f59e0b'); // Amber
        // Limit to first 3000 characters or so to avoid generating 100 pages of raw text, but let's give a nice representative portion
        const contentSnippet = file.content.length > 3000 
          ? `${file.content.substring(0, 3000)}\n\n[... DOCUMENT CONTENT TRUNCATED FOR REPORT PRESERVE ...]` 
          : file.content;
        addCodeSnippetBox(contentSnippet);
      }

      // --- 5. PAGE DECORATION & NUMBERS (Post-generation loop) ---
      const pageCount = (doc as any).internal.getNumberOfPages();
      for (let i = 1; i <= pageCount; i++) {
        doc.setPage(i);
        
        // Draw thin header line
        doc.setDrawColor(226, 232, 240); // slate-200
        doc.setLineWidth(0.3);
        doc.line(leftMargin, 15, 210 - rightMargin, 15);
        
        // Header text
        doc.setFont('helvetica', 'normal');
        doc.setFontSize(8);
        doc.setTextColor(100, 116, 139); // slate-500
        doc.text('WATCHTOWER AI-SYNC // INTELLIGENCE REPORT', leftMargin, 11);
        doc.text(`FILE ID: ${file.id}`, 210 - rightMargin, 11, { align: 'right' });

        // Draw footer line
        doc.line(leftMargin, 282, 210 - rightMargin, 282);
        
        // Footer text
        doc.text('CONFIDENTIAL - INTEL SYNC SECURITY LAYER', leftMargin, 287);
        doc.text(`Page ${i} of ${pageCount}`, 210 - rightMargin, 287, { align: 'right' });
      }

      // --- 6. SAVE PDF ---
      const sanitizedName = file.name.replace(/[^a-z0-9]/gi, '_').toLowerCase();
      doc.save(`watchtower_report_${sanitizedName}.pdf`);
      
      if (onLog) {
        onLog(`Successfully generated and downloaded PDF summary document for: ${file.name}`, 'success');
      }
    } catch (err: any) {
      console.error('PDF export failed:', err);
      if (onLog) {
        onLog(`PDF generation failed: ${err.message || err}`, 'error');
      }
    }
  };

  // Clear states when file changes
  useEffect(() => {
    setResult(null);
    setError(null);
    setAiSummary(null);
    setAiSummaryLoading(false);
    setAiSummaryError(null);
    setActiveTab('preview');
    setNewTag('');
  }, [file]);

  const handleGenerateAISummary = async () => {
    if (!file) return;
    setAiSummaryLoading(true);
    setAiSummaryError(null);
    onLog?.(`Initiating high-level bulleted summary generation for: "${file.name}"`, 'neural');
    try {
      const response = await fetch('/api/gemini/summarize-file', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          fileName: file.name,
          mimeType: file.mimeType,
          content: file.content,
        }),
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.error || 'Failed to generate AI summary');
      }

      const data = await response.json();
      setAiSummary(data.summary);
      onLog?.(`High-level AI summary successfully generated for "${file.name}"`, 'success');
    } catch (err: any) {
      console.error('Summary generation error:', err);
      const errMsg = err.message || 'Gemini summary generation failed.';
      setAiSummaryError(errMsg);
      onLog?.(`Summary generation failed for "${file.name}": ${errMsg}`, 'error');
    } finally {
      setAiSummaryLoading(false);
    }
  };

  const renderAISummaryContent = () => {
    if (aiSummaryLoading) {
      return (
        <div className="flex flex-col items-center justify-center text-center py-8 px-4 border border-slate-850 rounded-2xl bg-[#05070a]/20 min-h-[150px]" id="ai-summary-loading">
          <RefreshCw className="w-6 h-6 text-cyan-400 animate-spin mb-3" />
          <h5 className="text-xs font-bold text-slate-200 uppercase tracking-widest font-mono">Generating Bulleted Summary...</h5>
          <p className="text-[10px] text-slate-500 mt-1 font-mono">Processing document semantics</p>
        </div>
      );
    }

    if (aiSummaryError) {
      return (
        <div className="flex flex-col items-center justify-center text-center py-6 px-4 border border-rose-900/30 bg-rose-950/15 rounded-2xl min-h-[150px]" id="ai-summary-error">
          <AlertCircle className="w-8 h-8 text-rose-500 mb-2" />
          <h5 className="text-xs font-bold text-rose-400 uppercase tracking-wider font-mono">Generation Blocked</h5>
          <p className="text-[10px] text-rose-300 mt-1 max-w-sm leading-relaxed">{aiSummaryError}</p>
          <button
            type="button"
            onClick={handleGenerateAISummary}
            className="mt-3 px-3 py-1.5 bg-rose-600/20 hover:bg-rose-600/30 border border-rose-500 text-rose-400 text-[10px] font-bold rounded-lg transition-all uppercase tracking-wider cursor-pointer"
          >
            Retry Generation
          </button>
        </div>
      );
    }

    if (aiSummary) {
      const bullets = aiSummary
        .split('\n')
        .map(line => line.trim())
        .filter(line => line.startsWith('•') || line.startsWith('-') || line.length > 5)
        .map(line => line.replace(/^[•\-\*\s]+/, '').trim())
        .filter(line => line.length > 0);

      return (
        <div className="space-y-3 bg-cyan-950/10 border border-cyan-900/30 p-4 rounded-2xl" id="ai-summary-result">
          <div className="flex items-center justify-between pb-2 border-b border-cyan-950/50">
            <div className="flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-cyan-400 animate-pulse" />
              <span className="text-[10px] font-bold text-cyan-400 uppercase tracking-widest font-mono">High-Level Summary</span>
            </div>
            <button
              type="button"
              onClick={handleGenerateAISummary}
              className="text-[9px] font-bold font-mono text-slate-400 hover:text-cyan-400 transition-colors uppercase cursor-pointer"
              title="Regenerate bulleted summary"
            >
              Regenerate
            </button>
          </div>
          <ul className="space-y-2.5">
            {bullets.map((bullet, idx) => (
              <li key={idx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-300 leading-relaxed">
                <span className="text-cyan-400 mt-1 shrink-0 font-bold font-mono">⚡</span>
                <span>{bullet}</span>
              </li>
            ))}
          </ul>
        </div>
      );
    }

    return (
      <div className="flex flex-col items-center justify-center text-center py-8 px-4 border border-dashed border-slate-800 rounded-2xl bg-[#05070a]/40 min-h-[150px]" id="ai-summary-cta">
        <Sparkles className="w-8 h-8 text-cyan-400 mb-3 animate-pulse" />
        <h5 className="text-xs font-bold text-slate-200">Generate Bulleted AI Summary</h5>
        <p className="text-[10px] text-slate-400 mt-1.5 max-w-sm leading-relaxed font-mono">
          Extract 3-5 high-level bullet points summarizing the core essence of this file.
        </p>
        <button
          type="button"
          onClick={handleGenerateAISummary}
          className="mt-4 flex items-center gap-1.5 px-4 py-2 bg-cyan-600/20 hover:bg-cyan-600/30 border border-cyan-500 text-cyan-400 rounded-xl text-[10px] font-bold transition-all uppercase tracking-widest cursor-pointer"
          id="generate-ai-summary-btn"
        >
          <Sparkles className="w-3 h-3" />
          Generate AI Summary
        </button>
      </div>
    );
  };

  if (!file) return null;

  const handleAddTag = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTag.trim()) return;
    const tag = newTag.trim().toLowerCase();
    const currentTags = file.tags || [];
    if (!currentTags.includes(tag)) {
      const updated = [...currentTags, tag];
      onUpdateTags?.(file.id, updated);
      onLog?.(`Added custom label "${tag}" to "${file.name}"`, 'success');
    }
    setNewTag('');
  };

  const handleRemoveTag = (tagToRemove: string) => {
    const currentTags = file.tags || [];
    const updated = currentTags.filter(t => t !== tagToRemove);
    onUpdateTags?.(file.id, updated);
    onLog?.(`Removed custom label "${tagToRemove}" from "${file.name}"`, 'info');
  };

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    onLog?.(`Initiating Gemini content indexing & semantic mapping for: "${file.name}"`, 'neural');
    onLog?.(`Scanning structural text blocks (${file.content?.length || 0} characters extracted)`, 'system');
    try {
      const response = await fetch('/api/gemini/analyze-file', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          fileId: file.id,
          fileName: file.name,
          mimeType: file.mimeType,
          content: file.content,
        }),
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.error || 'Failed to analyze file');
      }

      const data = await response.json();
      setResult(data);
      onLog?.(`Gemini analysis synthesis successfully compiled for "${file.name}". Classification: ${data.projectCategory}`, 'success');
      // Automatically switch to insights tab if in compact mode so they can see the results immediately
      setActiveTab('insights');
    } catch (err: any) {
      console.error('Analysis error:', err);
      const errMsg = err.message || 'Gemini analysis failed. Please verify your GEMINI_API_KEY is active.';
      setError(errMsg);
      onLog?.(`Analysis failed for "${file.name}": ${errMsg}`, 'error');
    } finally {
      setLoading(false);
    }
  };

  const isDoc = file.mimeType.includes('document');
  const isSheet = file.mimeType.includes('spreadsheet');

  const renderInsightsContent = () => {
    if (!result && !loading && !error) {
      return (
        <div className="flex flex-col items-center justify-center text-center py-10 px-6 border border-dashed border-slate-800 rounded-2xl bg-[#05070a]/40 flex-1 min-h-[250px]" id="analyzer-core-cta">
          <Sparkles className="w-10 h-10 text-cyan-400 mb-4 animate-pulse" />
          <h4 className="text-sm font-bold text-slate-200">Intelligence Analyzer Core</h4>
          <p className="text-xs text-slate-400 mt-2 max-w-sm leading-relaxed">
            Connect this document with the live Gemini AI framework to automatically index keywords, compile executive summaries, and extract actionable checklists.
          </p>
          <button
            onClick={handleAnalyze}
            className="mt-5 flex items-center gap-2 px-5 py-2.5 bg-cyan-600/20 hover:bg-cyan-600/30 border border-cyan-500 text-cyan-400 rounded-xl text-xs font-bold transition-all uppercase tracking-widest cyber-glow-cyan cursor-pointer"
            id="trigger-analyze-file-btn"
          >
            <Sparkles className="w-3.5 h-3.5" />
            Analyze with Gemini
          </button>
        </div>
      );
    }

    if (loading) {
      return (
        <div className="flex flex-col items-center justify-center text-center py-12 px-6 border border-slate-850 rounded-2xl bg-[#05070a]/20 flex-1 min-h-[250px]" id="analyzer-loading-box">
          <RefreshCw className="w-8 h-8 text-cyan-400 animate-spin mb-4" />
          <h4 className="text-sm font-bold text-slate-200 uppercase tracking-widest">Compiling Intelligence Synthesis...</h4>
          <p className="text-xs text-slate-500 mt-1 font-mono">Invoking gemini-3.5-flash-core</p>
        </div>
      );
    }

    if (error) {
      return (
        <div className="flex flex-col items-center justify-center text-center py-10 px-6 border border-rose-900/30 bg-rose-950/15 rounded-2xl flex-1 min-h-[250px]" id="analyzer-error-box">
          <AlertCircle className="w-10 h-10 text-rose-500 mb-4" />
          <h4 className="text-sm font-bold text-rose-400 uppercase tracking-wider">Analysis Stream Blocked</h4>
          <p className="text-xs text-rose-300 mt-2 max-w-sm leading-relaxed">
            {error}
          </p>
          <button
            onClick={handleAnalyze}
            className="mt-4 px-4 py-2 bg-rose-600/20 hover:bg-rose-600/30 border border-rose-500 text-rose-400 text-xs font-bold rounded-xl transition-all uppercase tracking-wider cursor-pointer"
            id="retry-analyze-file-btn"
          >
            Retry Analysis
          </button>
        </div>
      );
    }

    if (result) {
      return (
        <div className="space-y-5 overflow-y-auto pr-1 flex-1 max-h-[500px] scrollbar-thin" id="analysis-insights-box">
          {/* Export Report Action Bar */}
          <div className="flex items-center justify-between pb-3 border-b border-slate-800/60 bg-[#070b13] p-3 rounded-xl border border-slate-850">
            <div className="flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-cyan-400 animate-pulse" />
              <span className="text-[10px] font-bold text-slate-300 uppercase tracking-widest font-mono">Report Ready</span>
            </div>
            <button
              type="button"
              onClick={handleExportToPDF}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-cyan-500/10 hover:bg-cyan-500/25 border border-cyan-500/30 text-cyan-400 hover:text-cyan-300 text-[10px] font-bold font-mono uppercase rounded-lg transition-all cursor-pointer"
              title="Export complete analysis report package to printable PDF"
              id="insights-export-pdf-btn"
            >
              <FileDown className="w-3.5 h-3.5" />
              Export to PDF
            </button>
          </div>

          {/* Executive Summary */}
          <div>
            <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest block mb-2 font-mono">Executive Summary</span>
            <p className="text-xs sm:text-sm text-slate-300 bg-cyan-950/20 border border-cyan-900/30 p-4 rounded-2xl leading-relaxed whitespace-pre-line">
              {result.summary}
            </p>
          </div>

          {/* Tag Category */}
          <div className="flex items-center gap-2">
            <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest font-mono">Classification:</span>
            <span className="flex items-center gap-1.5 px-3 py-1 bg-slate-900/80 text-slate-300 border border-slate-800 rounded-full text-xs font-bold font-mono">
              <Tag className="w-3.5 h-3.5 text-cyan-400" />
              {result.projectCategory}
              <span className="text-[10px] text-cyan-400">({result.categoryScore}%)</span>
            </span>
          </div>

          {/* Two Column Takeaways / Action Items */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {/* Key Takeaways */}
            <div>
              <div className="flex items-center gap-1.5 mb-2">
                <CheckSquare className="w-4 h-4 text-emerald-400" />
                <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest font-mono">Takeaways</span>
              </div>
              <ul className="space-y-2">
                {result.keyTakeaways.map((takeaway, idx) => (
                  <li key={idx} className="text-xs text-slate-300 bg-[#05070a]/60 border border-slate-850 p-2.5 rounded-xl leading-relaxed">
                    {takeaway}
                  </li>
                ))}
              </ul>
            </div>

            {/* Action Items */}
            <div>
              <div className="flex items-center gap-1.5 mb-2">
                <ListTodo className="w-4 h-4 text-cyan-400" />
                <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest font-mono">Action Items</span>
              </div>
              <ul className="space-y-2">
                {result.actionItems.map((action, idx) => (
                  <li key={idx} className="text-xs text-slate-300 bg-[#05070a]/60 border border-slate-850 p-2.5 rounded-xl leading-relaxed">
                    {action}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      );
    }

    return null;
  };

  return (
    <>
      {/* Backdrop */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
        className="fixed inset-0 bg-[#05070a]/75 backdrop-blur-xs z-50 cursor-pointer"
        id="file-analyzer-backdrop"
      />

      {/* Side Panel Drawer */}
      <motion.div
        initial={{ x: '100%' }}
        animate={{ x: 0 }}
        exit={{ x: '100%' }}
        transition={{ type: 'spring', damping: 30, stiffness: 300 }}
        className={`fixed inset-y-0 right-0 z-50 h-full bg-[#090d16]/95 border-l border-cyan-500/20 backdrop-blur-xl shadow-[0_0_50px_rgba(6,182,212,0.15)] flex flex-col transition-all duration-300 ${
          isExpanded 
            ? 'w-full lg:w-[85vw] xl:w-[75vw]' 
            : 'w-full sm:max-w-xl md:max-w-2xl'
        }`}
        id="file-analyzer-panel"
      >
        {/* Header */}
        <div className="p-6 border-b border-slate-800/80 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3 w-[calc(100%-100px)]">
            <span className={`p-2.5 rounded-xl border shrink-0 ${
              isDoc 
                ? 'bg-cyan-950/50 border-cyan-800/30 text-cyan-400' 
                : isSheet 
                  ? 'bg-emerald-950/50 border-emerald-800/30 text-emerald-400' 
                  : 'bg-amber-950/50 border-amber-800/30 text-amber-400'
            }`}>
              <FileText className="w-5 h-5" />
            </span>
            <div className="truncate flex-1">
              <h3 className="text-base font-bold text-slate-100 truncate leading-tight">{file.name}</h3>
              <div className="flex items-center gap-2.5 mt-1 flex-wrap">
                <span className="text-[10px] text-slate-400 font-mono uppercase tracking-wider truncate">
                  ID: {file.id} • {isDoc ? 'Google Doc' : isSheet ? 'Google Sheet' : 'Binary Spec'}
                </span>
                <span className="text-slate-800 text-[10px] select-none">•</span>
                <button
                  type="button"
                  onClick={() => setQuickViewOpen(true)}
                  className="inline-flex items-center gap-1 text-[10px] font-bold font-mono text-cyan-400 hover:text-cyan-300 transition-colors uppercase cursor-pointer animate-pulse"
                  title="Launch quick inline previewer"
                  id="header-quick-view-btn"
                >
                  <Eye className="w-3.5 h-3.5" />
                  Quick View
                </button>
                <span className="text-slate-800 text-[10px] select-none">•</span>
                <button
                  type="button"
                  onClick={handleShareFile}
                  className={`inline-flex items-center gap-1 text-[10px] font-bold font-mono transition-colors uppercase cursor-pointer ${
                    shareSuccess ? 'text-emerald-400 font-bold' : 'text-cyan-400 hover:text-cyan-300'
                  }`}
                  title="Share document link"
                  id="header-share-file-btn"
                >
                  {shareSuccess ? <Check className="w-3.5 h-3.5" /> : <Share2 className="w-3.5 h-3.5" />}
                  {shareSuccess ? 'Copied' : 'Share Link'}
                </button>
                <span className="text-slate-800 text-[10px] select-none">•</span>
                <button
                  type="button"
                  onClick={handleExportToPDF}
                  className="inline-flex items-center gap-1 text-[10px] font-bold font-mono text-cyan-400 hover:text-cyan-300 transition-colors uppercase cursor-pointer"
                  title="Export analysis summary to PDF"
                  id="header-export-pdf-btn"
                >
                  <FileDown className="w-3.5 h-3.5" />
                  Export PDF
                </button>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-1">
            {/* Quick View Top Action Button */}
            <button
              onClick={() => setQuickViewOpen(true)}
              className="p-2 hover:bg-slate-850 text-cyan-400 hover:text-cyan-300 rounded-lg transition-all cursor-pointer"
              title="Quick View Content"
              aria-label="Quick View Content"
              id="action-bar-quick-view-btn"
            >
              <Eye className="w-4 h-4" />
            </button>

            {/* Export PDF Action Button */}
            <button
              onClick={handleExportToPDF}
              className="p-2 hover:bg-slate-850 text-cyan-400 hover:text-cyan-300 rounded-lg transition-all cursor-pointer"
              title="Export analysis summary to PDF"
              aria-label="Export PDF"
              id="action-bar-export-pdf-btn"
            >
              <FileDown className="w-4 h-4" />
            </button>

            {/* Share File Button */}
            <button
              onClick={handleShareFile}
              className={`p-2 rounded-lg transition-all cursor-pointer border ${
                shareSuccess 
                  ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400' 
                  : 'hover:bg-slate-850 text-cyan-400 hover:text-cyan-300 border-transparent'
              }`}
              title={shareSuccess ? 'Copied to clipboard!' : 'Share File Link'}
              aria-label="Share File"
              id="action-bar-share-file-btn"
            >
              {shareSuccess ? <Check className="w-4 h-4" /> : <Share2 className="w-4 h-4" />}
            </button>

            {/* Expand/Collapse Toggle Button */}
            <button
              onClick={() => setIsExpanded(!isExpanded)}
              className="p-2 hover:bg-slate-850 text-slate-400 hover:text-slate-200 rounded-lg transition-all cursor-pointer"
              title={isExpanded ? 'Collapse side-panel size' : 'Expand side-panel size'}
              aria-label={isExpanded ? 'Collapse' : 'Expand'}
            >
              {isExpanded ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
            </button>

            {/* Close Button */}
            <button
              onClick={onClose}
              className="p-2 hover:bg-slate-850 text-slate-400 hover:text-rose-400 rounded-lg transition-all cursor-pointer"
              id="close-analyzer-btn"
              aria-label="Close"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Dynamic Scan line overlay */}
        <div className="scanline absolute top-0 left-0 w-full h-1 bg-cyan-500/20 pointer-events-none opacity-40 z-10"></div>

        {/* Main Content Scrollable Area */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6" id="drawer-scrollable-content">
          {/* Custom Tag Management Panel */}
          <div className="bg-[#05070a]/40 border border-slate-850 p-4 rounded-2xl flex flex-col gap-3" id="file-tag-manager">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 text-slate-300">
                <Tag className="w-4 h-4 text-cyan-400" />
                <span className="text-xs font-bold uppercase tracking-wider font-mono">Custom Labels & Tags</span>
              </div>
              <span className="text-[10px] text-slate-500 font-mono">Manual Tagging</span>
            </div>

            {/* Current Tags List */}
            <div className="flex flex-wrap gap-1.5 min-h-[28px]">
              {file.tags && file.tags.length > 0 ? (
                file.tags.map((tag) => (
                  <span
                    key={tag}
                    className="flex items-center gap-1.5 px-2 py-0.5 bg-cyan-950/30 border border-cyan-800/40 text-cyan-300 rounded-md text-[10px] font-mono"
                  >
                    {tag}
                    <button
                      type="button"
                      onClick={() => handleRemoveTag(tag)}
                      className="hover:text-rose-400 transition-colors cursor-pointer text-slate-500 font-bold ml-1"
                      title={`Remove tag: ${tag}`}
                    >
                      &times;
                    </button>
                  </span>
                ))
              ) : (
                <span className="text-xs text-slate-500 italic font-mono self-center">No tags assigned. Add a custom tag below.</span>
              )}
            </div>

            {/* Add New Tag Input Form */}
            <form onSubmit={handleAddTag} className="flex gap-2">
              <input
                type="text"
                placeholder="Enter custom label (e.g., Q3-report, draft, archive)..."
                value={newTag}
                onChange={(e) => setNewTag(e.target.value)}
                className="flex-1 px-3 py-1.5 bg-[#030508] border border-slate-800 rounded-lg text-xs text-slate-300 placeholder-slate-600 focus:ring-1 focus:ring-cyan-500 focus:outline-hidden font-mono"
                id="new-tag-input"
              />
              <button
                type="submit"
                className="px-3.5 py-1.5 bg-cyan-600/10 hover:bg-cyan-600/20 border border-cyan-500/30 text-cyan-400 rounded-lg text-xs font-bold font-mono uppercase tracking-wider transition-all cursor-pointer"
              >
                Add
              </button>
            </form>
          </div>

          {isExpanded ? (
            /* Side-by-Side dual column layout for expanded view */
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">
              {/* Left Column: Raw Preview */}
              <div className="flex flex-col space-y-3" id="file-raw-content-preview">
                <div className="flex items-center justify-between pb-1">
                  <span className="text-[10px] font-bold text-slate-500 tracking-widest uppercase font-mono">Telemetry Spec Stream</span>
                  <div className="flex items-center gap-2.5">
                    <button
                      type="button"
                      onClick={() => setQuickViewOpen(true)}
                      className="flex items-center gap-1.5 px-2.5 py-1 bg-cyan-600/10 hover:bg-cyan-600/20 border border-cyan-500/30 text-cyan-400 text-[10px] font-bold font-mono uppercase rounded-md transition-all cursor-pointer"
                      title="Launch quick interactive reader"
                    >
                      <Eye className="w-3.5 h-3.5" />
                      Full Reader
                    </button>
                    <span className="text-[10px] text-slate-500 font-mono">{(file.content?.length || 0) > 0 ? `${file.content!.length} chars` : '0 chars'}</span>
                  </div>
                </div>
                <div className="bg-[#05070a]/60 border border-slate-850 rounded-2xl p-4 overflow-y-auto text-xs text-slate-300 font-mono leading-relaxed whitespace-pre-line max-h-[550px] scrollbar-thin">
                  {file.content ? (
                    file.content.trim()
                  ) : (
                    <span className="text-slate-600 italic">No telemetry data stream extracted. Content empty.</span>
                  )}
                </div>
              </div>

              {/* Right Column: AI Insights & Summary */}
              <div className="flex flex-col space-y-5" id="file-intelligence-insights">
                <div className="flex flex-col space-y-3">
                  <div className="flex items-center justify-between pb-1">
                    <span className="text-[10px] font-bold text-slate-500 tracking-widest uppercase font-mono">AI High-Level Summary</span>
                  </div>
                  {renderAISummaryContent()}
                </div>

                <div className="flex flex-col space-y-3">
                  <div className="flex items-center justify-between pb-1">
                    <span className="text-[10px] font-bold text-slate-500 tracking-widest uppercase font-mono">Personal Intelligence Insights</span>
                  </div>
                  {renderInsightsContent()}
                </div>
              </div>
            </div>
          ) : (
            /* Segmented tabbed view for Compact Mode */
            <div className="flex flex-col space-y-5">
              {/* Segmented Tab controls */}
              <div className="flex bg-[#05070a] border border-slate-850 p-1 rounded-xl gap-1">
                <button
                  type="button"
                  onClick={() => setActiveTab('preview')}
                  className={`flex-1 py-2 text-center text-[11px] font-bold uppercase tracking-wider rounded-lg transition-all cursor-pointer ${
                    activeTab === 'preview'
                      ? 'bg-cyan-600/20 border border-cyan-500/30 text-cyan-400'
                      : 'text-slate-500 hover:text-slate-300'
                  }`}
                >
                  Telemetry
                </button>
                <button
                  type="button"
                  onClick={() => setActiveTab('insights')}
                  className={`flex-1 py-2 text-center text-[11px] font-bold uppercase tracking-wider rounded-lg transition-all cursor-pointer ${
                    activeTab === 'insights'
                      ? 'bg-cyan-600/20 border border-cyan-500/30 text-cyan-400'
                      : 'text-slate-500 hover:text-slate-300'
                  }`}
                >
                  AI Insights
                </button>
                <button
                  type="button"
                  onClick={() => setActiveTab('summary')}
                  className={`flex-1 py-2 text-center text-[11px] font-bold uppercase tracking-wider rounded-lg transition-all cursor-pointer ${
                    activeTab === 'summary'
                      ? 'bg-cyan-600/20 border border-cyan-500/30 text-cyan-400'
                      : 'text-slate-500 hover:text-slate-300'
                  }`}
                >
                  AI Summary
                </button>
              </div>

              {/* Tab views */}
              <div className="min-h-[300px] flex flex-col">
                {activeTab === 'preview' ? (
                  <div className="flex flex-col space-y-3" id="file-raw-content-preview">
                    <div className="flex items-center justify-between pb-1">
                      <span className="text-[10px] font-bold text-slate-500 tracking-widest uppercase font-mono">Telemetry Spec Stream</span>
                      <div className="flex items-center gap-2.5">
                        <button
                          type="button"
                          onClick={() => setQuickViewOpen(true)}
                          className="flex items-center gap-1.5 px-2.5 py-1 bg-cyan-600/10 hover:bg-cyan-600/20 border border-cyan-500/30 text-cyan-400 text-[10px] font-bold font-mono uppercase rounded-md transition-all cursor-pointer"
                          title="Launch quick interactive reader"
                        >
                          <Eye className="w-3.5 h-3.5" />
                          Full Reader
                        </button>
                        <span className="text-[10px] text-slate-500 font-mono">{(file.content?.length || 0) > 0 ? `${file.content!.length} chars` : '0 chars'}</span>
                      </div>
                    </div>
                    <div className="bg-[#05070a]/60 border border-slate-850 rounded-2xl p-4 overflow-y-auto text-xs text-slate-300 font-mono leading-relaxed whitespace-pre-line max-h-[480px] scrollbar-thin">
                      {file.content ? (
                        file.content.trim()
                      ) : (
                        <span className="text-slate-600 italic">No telemetry data stream extracted. Content empty.</span>
                      )}
                    </div>
                  </div>
                ) : activeTab === 'summary' ? (
                  <div className="flex flex-col space-y-3" id="file-ai-summary">
                    <div className="flex items-center justify-between pb-1">
                      <span className="text-[10px] font-bold text-slate-500 tracking-widest uppercase font-mono">AI High-Level Summary</span>
                    </div>
                    {renderAISummaryContent()}
                  </div>
                ) : (
                  <div className="flex flex-col space-y-3" id="file-intelligence-insights">
                    {renderInsightsContent()}
                  </div>
                )}
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="p-6 border-t border-slate-800/80 flex items-center justify-between bg-[#05070a]/40 shrink-0">
          <span className="text-[9px] text-slate-500 font-mono uppercase tracking-wider">Secure Sandbox Connection // Active</span>
          <button
            onClick={onClose}
            className="px-4 py-2 bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 text-slate-300 rounded-xl text-xs font-bold transition-all cursor-pointer"
          >
            Close Preview
          </button>
        </div>
      </motion.div>

      {/* Lightweight Quick View Modal */}
      <AnimatePresence>
        {quickViewOpen && (
          <div className="fixed inset-0 z-[120] flex items-center justify-center p-4 sm:p-6" id="quick-view-modal-container">
            {/* Modal Backdrop */}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setQuickViewOpen(false)}
              className="fixed inset-0 bg-[#030508]/85 backdrop-blur-md cursor-pointer"
              id="quick-view-modal-backdrop"
            />

            {/* Modal Content */}
            <motion.div
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.95, opacity: 0 }}
              transition={{ type: 'spring', duration: 0.3 }}
              className="relative w-full max-w-4xl h-[85vh] bg-[#090d16] border border-cyan-500/30 rounded-3xl shadow-[0_0_50px_rgba(6,182,212,0.25)] flex flex-col overflow-hidden z-10"
              id="quick-view-modal-content"
            >
              {/* Modal Header */}
              <div className="p-5 sm:p-6 border-b border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-4 shrink-0 bg-[#05070a]/40">
                <div className="flex items-center gap-3">
                  <span className={`p-2 rounded-lg border ${
                    isDoc 
                      ? 'bg-cyan-950/40 border-cyan-800/30 text-cyan-400' 
                      : isSheet 
                        ? 'bg-emerald-950/40 border-emerald-800/30 text-emerald-400' 
                        : 'bg-amber-950/40 border-amber-800/30 text-amber-400'
                  }`}>
                    {isSheet ? <FileSpreadsheet className="w-4 h-4" /> : <FileText className="w-4 h-4" />}
                  </span>
                  <div>
                    <h3 className="text-sm font-bold text-slate-100 flex items-center gap-2">
                      Quick View Reader
                      <span className="text-[10px] text-slate-500 font-mono font-normal">({file.name})</span>
                    </h3>
                    <p className="text-[10px] text-slate-400 font-mono uppercase tracking-wider mt-0.5">
                      Type: {isDoc ? 'Google Doc' : isSheet ? 'Google Sheet' : 'Raw Stream'}
                    </p>
                  </div>
                </div>

                {/* View Mode Switching Controls */}
                <div className="flex items-center gap-3">
                  <div className="flex bg-[#030508] border border-slate-800 p-0.5 rounded-lg text-[10px] font-mono">
                    <button
                      type="button"
                      onClick={() => setViewerMode('dedicated')}
                      className={`px-3 py-1.5 font-bold uppercase rounded-md transition-all cursor-pointer ${
                        viewerMode === 'dedicated'
                          ? 'bg-cyan-600/20 text-cyan-400 border border-cyan-500/30'
                          : 'text-slate-500 hover:text-slate-300'
                      }`}
                    >
                      Dedicated Viewer
                    </button>
                    <button
                      type="button"
                      onClick={() => setViewerMode('iframe')}
                      className={`px-3 py-1.5 font-bold uppercase rounded-md transition-all cursor-pointer ${
                        viewerMode === 'iframe'
                          ? 'bg-cyan-600/20 text-cyan-400 border border-cyan-500/30'
                          : 'text-slate-500 hover:text-slate-300'
                      }`}
                    >
                      Interactive Sandbox
                    </button>
                  </div>

                  {/* Share button */}
                  <button
                    onClick={handleShareFile}
                    className={`p-2 rounded-lg transition-all cursor-pointer border ${
                      shareSuccess 
                        ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400' 
                        : 'hover:bg-slate-800 text-cyan-400 hover:text-cyan-300 border-transparent'
                    }`}
                    title={shareSuccess ? 'Copied!' : 'Share File'}
                    aria-label="Share File"
                  >
                    {shareSuccess ? <Check className="w-4 h-4" /> : <Share2 className="w-4 h-4" />}
                  </button>

                  {/* Close button */}
                  <button
                    onClick={() => setQuickViewOpen(false)}
                    className="p-2 hover:bg-slate-800 text-slate-400 hover:text-rose-400 rounded-lg transition-all cursor-pointer"
                    aria-label="Close Quick View"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>

              {/* Modal Body */}
              <div className="flex-1 overflow-y-auto p-6 bg-[#030508]/30">
                {viewerMode === 'dedicated' ? (
                  <div className="h-full flex flex-col" id="dedicated-view-pane">
                    {isSheet ? (
                      /* EXCEL-LIKE RICH DATA GRID VIEWER */
                      <div className="flex-1 flex flex-col border border-slate-800/80 rounded-2xl overflow-hidden bg-[#05070a]/60">
                        {/* Spreadsheet Grid Title */}
                        <div className="px-4 py-2 bg-slate-900/60 border-b border-slate-800 flex items-center justify-between text-[11px] font-mono">
                          <span className="text-emerald-400 font-bold flex items-center gap-1.5">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                            {(() => {
                              const match = file.content?.match(/Sheet Name:\s*(.*)/);
                              return match ? match[1].trim() : "Sheet_1.csv";
                            })()}
                          </span>
                          <span className="text-slate-500">Read-Only Grid Mode</span>
                        </div>

                        {/* Interactive Grid Table */}
                        <div className="flex-1 overflow-auto scrollbar-thin">
                          <table className="w-full text-left border-collapse font-mono text-[11px] text-slate-300">
                            <thead>
                              <tr className="bg-slate-900/40 border-b border-slate-850 select-none">
                                <th className="w-10 px-3 py-2 border-r border-slate-850 text-slate-500 text-center font-bold">#</th>
                                {(() => {
                                  const lines = file.content?.split('\n').map(l => l.trim()).filter(Boolean) || [];
                                  const firstRowLine = lines.find(line => line.match(/^Row \d+:/));
                                  const cellCount = firstRowLine 
                                    ? firstRowLine.replace(/^Row \d+:\s*/, '').split(',').length 
                                    : 4;
                                  return Array.from({ length: cellCount }).map((_, idx) => (
                                    <th key={idx} className="px-4 py-2 border-r border-slate-850 text-slate-400 font-bold text-center">
                                      {String.fromCharCode(65 + idx)}
                                    </th>
                                  ));
                                })()}
                              </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-850/60">
                              {(() => {
                                const lines = file.content?.split('\n').map(l => l.trim()).filter(Boolean) || [];
                                const rows: string[][] = [];
                                lines.forEach(line => {
                                  if (line.match(/^Row \d+:/)) {
                                    const cells = line.replace(/^Row \d+:\s*/, '').split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/).map(c => c.trim().replace(/^"|"$/g, ''));
                                    rows.push(cells);
                                  } else if (!line.startsWith('Sheet Name:')) {
                                    const cells = line.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/).map(c => c.trim().replace(/^"|"$/g, ''));
                                    if (cells.length > 0 && cells[0]) rows.push(cells);
                                  }
                                });

                                if (rows.length === 0) {
                                  return (
                                    <tr>
                                      <td colSpan={10} className="py-12 text-center text-slate-500 italic">
                                        No structured spreadsheet rows detected in content stream.
                                      </td>
                                    </tr>
                                  );
                                }

                                return rows.map((cells, rowIdx) => (
                                  <tr key={rowIdx} className="hover:bg-cyan-500/5 transition-colors duration-150">
                                    <td className="px-3 py-2 border-r border-slate-850 text-slate-500 font-bold text-center select-none bg-slate-900/15">
                                      {rowIdx + 1}
                                    </td>
                                    {cells.map((cell, colIdx) => (
                                      <td key={colIdx} className="px-4 py-2 border-r border-slate-850 truncate max-w-[200px]" title={cell}>
                                        <span className={rowIdx === 0 ? "font-bold text-slate-100" : ""}>{cell}</span>
                                      </td>
                                    ))}
                                  </tr>
                                ));
                              })()}
                            </tbody>
                          </table>
                        </div>
                      </div>
                    ) : isDoc ? (
                      /* ELEGANT PAPER COMPACT DOCUMENT VIEWER */
                      <div className="max-w-2xl mx-auto bg-slate-50 text-slate-800 shadow-2xl p-8 sm:p-12 rounded-xl border border-slate-200/80 min-h-[500px] font-sans relative overflow-hidden" id="document-paper-reader">
                        {/* Decorative binder punching */}
                        <div className="absolute left-3 top-0 bottom-0 flex flex-col justify-around py-8 pointer-events-none opacity-20">
                          <div className="w-3.5 h-3.5 rounded-full bg-slate-950 border border-slate-400 shadow-inner" />
                          <div className="w-3.5 h-3.5 rounded-full bg-slate-950 border border-slate-400 shadow-inner" />
                          <div className="w-3.5 h-3.5 rounded-full bg-slate-950 border border-slate-400 shadow-inner" />
                        </div>

                        {/* Top Docket Header */}
                        <div className="border-b-2 border-slate-300 pb-4 mb-6 font-mono text-[9px] text-slate-500 uppercase tracking-wider flex justify-between">
                          <span>Watchtower Document Docket // Secure Sandbox</span>
                          <span>Last Refreshed: {new Date(file.modifiedTime).toLocaleDateString()}</span>
                        </div>

                        {/* Render parsed text paragraphs */}
                        <div className="space-y-4 max-h-[480px] overflow-y-auto pr-2 scrollbar-thin select-text">
                          {file.content ? (
                            file.content.split('\n').map((line, idx) => {
                              const trimmed = line.trim();
                              if (trimmed.startsWith('# ')) {
                                return <h1 key={idx} className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight border-b border-slate-200 pb-2 mb-4 mt-2 font-sans">{trimmed.replace('# ', '')}</h1>;
                              }
                              if (trimmed.startsWith('## ')) {
                                return <h2 key={idx} className="text-sm sm:text-base font-black text-slate-850 mb-3 mt-5 uppercase tracking-wide font-sans">{trimmed.replace('## ', '')}</h2>;
                              }
                              if (trimmed.startsWith('- ')) {
                                return <li key={idx} className="text-xs sm:text-sm text-slate-700 ml-5 list-disc mb-1.5 leading-relaxed">{trimmed.replace('- ', '')}</li>;
                              }
                              if (!trimmed) {
                                return <div key={idx} className="h-2.5" />;
                              }
                              return <p key={idx} className="text-xs sm:text-sm text-slate-700 leading-relaxed mb-3.5 font-sans font-normal">{trimmed}</p>;
                            })
                          ) : (
                            <p className="text-sm text-slate-400 italic text-center py-10">This document's content stream is empty.</p>
                          )}
                        </div>
                      </div>
                    ) : (
                      /* TERMINAL SPECS VIEWER FOR BINARY FILES */
                      <div className="flex-1 flex flex-col border border-slate-800 rounded-2xl overflow-hidden bg-[#05070a]/80 font-mono text-xs">
                        <div className="px-4 py-2 bg-slate-900 border-b border-slate-800 text-[10px] text-amber-400 font-bold flex items-center justify-between">
                          <span className="flex items-center gap-1.5">
                            <AlertCircle className="w-3.5 h-3.5" />
                            BINARY STREAM DISASSEMBLER
                          </span>
                          <span className="text-slate-500">Telemetry Spec Mode</span>
                        </div>
                        <div className="flex-1 p-5 overflow-auto text-slate-400 leading-relaxed max-h-[450px] scrollbar-thin">
                          <div className="text-cyan-500 font-bold mb-3">// SCAN DETAILS:</div>
                          <div className="grid grid-cols-3 gap-y-1 max-w-sm mb-5 text-[11px] text-slate-300 font-mono">
                            <span className="text-slate-500">File ID:</span>
                            <span className="col-span-2 text-slate-200">{file.id}</span>
                            <span className="text-slate-500">Mime Type:</span>
                            <span className="col-span-2 text-slate-200">{file.mimeType}</span>
                            <span className="text-slate-500">Data Size:</span>
                            <span className="col-span-2 text-slate-200">{file.size ? `${(file.size / 1024).toFixed(2)} KB` : 'Unknown'}</span>
                          </div>
                          
                          <div className="text-cyan-500 font-bold mb-2">// TELEMETRY CONTENT PREVIEW:</div>
                          <div className="bg-[#030508] p-4 rounded-xl border border-slate-850/80 text-slate-300 whitespace-pre-wrap">
                            {file.content || 'No text snippet found for this asset type.'}
                          </div>
                        </div>
                      </div>
                    )}
                  </div>
                ) : (
                  /* IFRAME EMBEDDED PREVIEW MODE */
                  <div className="h-full flex flex-col space-y-4" id="iframe-view-pane">
                    {/* Security Warning Banner */}
                    <div className="flex items-start gap-3 p-4 bg-cyan-950/20 border border-cyan-800/40 rounded-2xl text-[11px] text-cyan-300" id="iframe-security-toast">
                      <Info className="w-4 h-4 shrink-0 text-cyan-400 mt-0.5" />
                      <div className="leading-relaxed">
                        <p className="font-bold">Google Iframe Sandbox</p>
                        <p className="mt-0.5 text-slate-400">
                          Due to tight browser cookie isolation and frame policies in Google's ecosystem, some files might require sign-in to display or display a generic error.
                          If the iframe fails to load, you can click <span className="font-bold text-cyan-400">"Dedicated Viewer"</span> above for a structured text view, or use the direct link below.
                        </p>
                      </div>
                    </div>

                    {/* The sandbox frame container */}
                    <div className="flex-1 border border-slate-800/80 bg-slate-950 rounded-2xl overflow-hidden relative min-h-[350px]">
                      <iframe
                        src={(() => {
                          // Construct standard Google Doc/Sheet /preview link to bypass full edit wrapper
                          if (file.mimeType.includes('document')) {
                            return `https://docs.google.com/document/d/${file.id}/preview`;
                          }
                          if (file.mimeType.includes('spreadsheet')) {
                            return `https://docs.google.com/spreadsheets/d/${file.id}/preview`;
                          }
                          return `https://drive.google.com/file/d/${file.id}/preview`;
                        })()}
                        className="w-full h-full border-none"
                        title={`Embedded preview of ${file.name}`}
                        allow="autoplay"
                        sandbox="allow-scripts allow-same-origin allow-popups"
                        referrerPolicy="no-referrer"
                      />
                    </div>

                    {/* External Link Fallback Trigger */}
                    <div className="flex items-center justify-between px-2">
                      <span className="text-[10px] text-slate-500 font-mono">FRAME ENDPOINT: docs.google.com/d/{file.id}</span>
                      <div className="flex items-center gap-2">
                        <button
                          type="button"
                          onClick={handleShareFile}
                          className={`inline-flex items-center gap-1.5 px-4 py-2 border rounded-xl text-xs font-bold transition-all cursor-pointer ${
                            shareSuccess 
                              ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400' 
                              : 'bg-slate-900 hover:bg-slate-850 text-cyan-400 hover:text-cyan-300 border-slate-800'
                          }`}
                        >
                          {shareSuccess ? <Check className="w-3.5 h-3.5" /> : <Share2 className="w-3.5 h-3.5" />}
                          {shareSuccess ? 'Link Copied' : 'Share Link'}
                        </button>
                        {file.webViewLink && (
                          <a
                            href={file.webViewLink}
                            target="_blank"
                            rel="noreferrer noopener"
                            className="inline-flex items-center gap-1.5 px-4 py-2 bg-slate-900 hover:bg-slate-850 text-cyan-400 hover:text-cyan-300 border border-slate-800 rounded-xl text-xs font-bold transition-all"
                          >
                            <ExternalLink className="w-3.5 h-3.5" />
                            Open in Google Drive
                          </a>
                        )}
                      </div>
                    </div>
                  </div>
                )}
              </div>

              {/* Modal Footer */}
              <div className="p-4 sm:p-5 border-t border-slate-800/80 flex items-center justify-between shrink-0 bg-[#05070a]/40 font-mono text-[9px] text-slate-500 uppercase tracking-widest">
                <span>SANDBOX READ-ONLY STREAM</span>
                <button
                  type="button"
                  onClick={() => setQuickViewOpen(false)}
                  className="px-4 py-2 bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 text-slate-300 rounded-xl text-xs font-bold transition-all cursor-pointer font-sans normal-case"
                >
                  Close Viewer
                </button>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </>
  );
}
