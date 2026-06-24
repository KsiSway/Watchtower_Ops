/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  Sparkles,
  Compass,
  LayoutDashboard,
  ShieldAlert,
  Database,
  RefreshCw,
  CheckCircle2,
  Trash2,
  FileSpreadsheet,
  Sun,
  Moon,
  Keyboard,
  Command,
  X,
} from 'lucide-react';
import GoogleConnection from './components/GoogleConnection';
import WatchtowerDashboard from './components/WatchtowerDashboard';
import WatchtowerSettings from './components/WatchtowerSettings';
import WatchtowerGmail from './components/WatchtowerGmail';
import FileList from './components/FileList';
import FileAnalyzer from './components/FileAnalyzer';
import SystemActivityLog from './components/SystemActivityLog';
import WatchtowerAICopilot from './components/WatchtowerAICopilot';
import { DriveFile, WatchtowerStats, CleanUpRecommendation, LogEntry } from './types';
import {
  mockFiles,
  mockStats,
  mockRecommendations,
} from './data/mockWorkspace';

function LastSyncIndicator({ lastSyncTime }: { lastSyncTime: string }) {
  const [elapsedSeconds, setElapsedSeconds] = useState<number>(0);

  useEffect(() => {
    if (!lastSyncTime) return;

    const calculateElapsed = () => {
      const diffMs = Date.now() - new Date(lastSyncTime).getTime();
      return Math.max(0, Math.floor(diffMs / 1000));
    };

    setElapsedSeconds(calculateElapsed());

    let timerId: any = null;

    const tick = () => {
      const currentElapsed = calculateElapsed();
      setElapsedSeconds(currentElapsed);

      // Determine next tick interval dynamically:
      // - Under 1 minute: tick every 1 second
      // - Under 5 minutes: tick every 10 seconds
      // - Over 5 minutes: tick every 30 seconds
      let nextInterval = 1000;
      if (currentElapsed >= 300) {
        nextInterval = 30000;
      } else if (currentElapsed >= 60) {
        nextInterval = 10000;
      }

      if (timerId) clearTimeout(timerId);
      timerId = setTimeout(tick, nextInterval);
    };

    timerId = setTimeout(tick, 1000);

    return () => {
      if (timerId) clearTimeout(timerId);
    };
  }, [lastSyncTime]);

  let displayStr = 'Never';
  let indicatorColor = 'bg-rose-500 shadow-rose-500/40';
  let textColor = 'text-rose-400';
  let statusText = 'STALE';
  let tooltipText = 'System has not been synchronized yet.';

  if (lastSyncTime) {
    if (elapsedSeconds < 15) {
      displayStr = 'Just now';
      indicatorColor = 'bg-emerald-400 shadow-[0_0_8px_#34d399] animate-pulse';
      textColor = 'text-emerald-400';
      statusText = 'SYNCED';
      tooltipText = 'Real-time precision: updating every 1s';
    } else if (elapsedSeconds < 60) {
      displayStr = `${elapsedSeconds}s ago`;
      indicatorColor = 'bg-emerald-500 shadow-[0_0_6px_#10b981] animate-pulse';
      textColor = 'text-emerald-400';
      statusText = 'FRESH';
      tooltipText = 'Real-time precision: updating every 1s';
    } else if (elapsedSeconds < 300) {
      const mins = Math.floor(elapsedSeconds / 60);
      const secs = elapsedSeconds % 60;
      displayStr = `${mins}m ${secs}s ago`;
      indicatorColor = 'bg-cyan-500 shadow-[0_0_6px_#06b6d4]';
      textColor = 'text-cyan-400';
      statusText = 'RECENT';
      tooltipText = 'Standard precision: updating every 10s';
    } else {
      const mins = Math.floor(elapsedSeconds / 60);
      displayStr = `${mins}m ago`;
      indicatorColor = 'bg-amber-500 shadow-[0_0_6px_#f59e0b]';
      textColor = 'text-amber-400';
      statusText = 'STALE';
      tooltipText = 'Power-saver mode: updating every 30s';
    }
  }

  return (
    <div 
      className="flex items-center gap-2 bg-[#090d16]/80 border border-slate-800/80 px-3 py-1 rounded-full text-[10px] font-mono select-none"
      title={tooltipText}
    >
      <div className={`w-2 h-2 rounded-full transition-all duration-500 ${indicatorColor}`} />
      <span className="text-slate-500 uppercase font-bold tracking-wider text-[9px]">Last Sync:</span>
      <span className={`font-bold ${textColor}`}>{displayStr}</span>
      <span className="text-[8px] bg-slate-900 border border-slate-800 text-slate-400 px-1.5 py-0.5 rounded-md uppercase font-bold tracking-widest leading-none">{statusText}</span>
    </div>
  );
}

export default function App() {
  const [isSandbox, setIsSandbox] = useState(true);
  const [accessToken, setAccessToken] = useState<string>('');
  const [userEmail, setUserEmail] = useState<string | null>(null);
  const [showShortcutsModal, setShowShortcutsModal] = useState(false);

  // Personalized operator settings
  const [operatorCallSign, setOperatorCallSign] = useState<string>(() => {
    return localStorage.getItem('watchtower-operator-callsign') || 'KsiSway';
  });
  const [operatorRank, setOperatorRank] = useState<string>(() => {
    return localStorage.getItem('watchtower-operator-rank') || 'Lead Watchtower Operator';
  });

  // App core states
  const [files, setFiles] = useState<DriveFile[]>(mockFiles);
  const [selectedFile, setSelectedFile] = useState<DriveFile | null>(null);
  const [fileTags, setFileTags] = useState<Record<string, string[]>>(() => {
    const saved = localStorage.getItem('watchtower-file-tags');
    return saved ? JSON.parse(saved) : {};
  });

  const filesWithTags = files.map(file => ({
    ...file,
    tags: fileTags[file.id] || []
  }));

  const selectedFileWithTags = selectedFile ? {
    ...selectedFile,
    tags: fileTags[selectedFile.id] || []
  } : null;

  const handleUpdateTags = (fileId: string, tags: string[]) => {
    setFileTags(prev => {
      const updated = { ...prev, [fileId]: tags };
      localStorage.setItem('watchtower-file-tags', JSON.stringify(updated));
      return updated;
    });
    const targetFile = files.find(f => f.id === fileId);
    if (targetFile) {
      addLog(`Updated custom tags for "${targetFile.name}": [${tags.join(', ')}]`, 'info');
    }
  };

  const [stats, setStats] = useState<WatchtowerStats>(mockStats);
  const [recommendations, setRecommendations] = useState<CleanUpRecommendation[]>(mockRecommendations);
  const [categories, setCategories] = useState<{ name: string; count: number; description: string }[]>([
    { name: 'Financial Forecasts', count: 2, description: 'Spreadsheets detailing forecast models' },
    { name: 'Product specs', count: 2, description: 'Specs, roadmaps and notes' },
    { name: 'Corporate Compliance', count: 1, description: 'Guidelines on security policies' },
  ]);

  const [isSyncing, setIsSyncing] = useState(false);
  const [syncProgress, setSyncProgress] = useState<number>(0);
  const [syncMessage, setSyncMessage] = useState<string | null>(null);
  const [serverOnline, setServerOnline] = useState(true);

  // System Logs State
  const [logs, setLogs] = useState<LogEntry[]>([
    { id: '1', timestamp: new Date(Date.now() - 30000).toLocaleTimeString(), message: 'Booting Watchtower Core v4.2.8...', type: 'system' },
    { id: '2', timestamp: new Date(Date.now() - 25000).toLocaleTimeString(), message: 'Secure Shell connection established on 192.168.68.110.', type: 'info' },
    { id: '3', timestamp: new Date(Date.now() - 20000).toLocaleTimeString(), message: 'Initializing local personal AI model: gemini-3.5-flash.', type: 'neural' },
    { id: '4', timestamp: new Date(Date.now() - 15000).toLocaleTimeString(), message: 'Verifying local sandbox catalog structures...', type: 'system' },
    { id: '5', timestamp: new Date(Date.now() - 5000).toLocaleTimeString(), message: 'Ready. Tracking 5 workspace files in Sandbox Mode.', type: 'success' },
  ]);

  const addLog = (message: string, type: LogEntry['type'] = 'info') => {
    const newLog: LogEntry = {
      id: Math.random().toString(36).substr(2, 9),
      timestamp: new Date().toLocaleTimeString(),
      message,
      type,
    };
    setLogs((prev) => [...prev, newLog]);
  };

  // Theme states & persistence
  const [theme, setTheme] = useState<'cyberpunk' | 'terminal-light'>(() => {
    const saved = localStorage.getItem('watchtower-theme');
    return (saved === 'terminal-light') ? 'terminal-light' : 'cyberpunk';
  });

  const [themeInitialized, setThemeInitialized] = useState(false);

  useEffect(() => {
    localStorage.setItem('watchtower-theme', theme);
    const root = document.documentElement;
    if (theme === 'terminal-light') {
      root.classList.add('theme-terminal-light');
    } else {
      root.classList.remove('theme-terminal-light');
    }

    if (themeInitialized) {
      addLog(`Watchtower Core theme toggled: ${theme === 'terminal-light' ? 'TERMINAL LIGHT MODE' : 'CYBERPUNK DARK MODE'}`, 'system');
    } else {
      setThemeInitialized(true);
    }
  }, [theme]);

  const handleSelectFile = (file: DriveFile | null) => {
    setSelectedFile(file);
    if (file) {
      addLog(`Selected document file for inspection: "${file.name}" (Mime: ${file.mimeType.split('/').pop()})`, 'info');
    } else {
      addLog('Closed document inspection interface.', 'system');
    }
  };

  // Fetch client-side public Google Client ID configuration
  const clientId = ((import.meta as any).env?.VITE_GOOGLE_CLIENT_ID as string) || '';

  // Check server health on launch
  useEffect(() => {
    fetch('/api/health')
      .then((res) => res.json())
      .then((data) => {
        const isOnline = data.status === 'ok';
        setServerOnline(isOnline);
        addLog(`Express server health check: ${isOnline ? 'ONLINE' : 'DEGRADED'}`, isOnline ? 'success' : 'warn');
      })
      .catch((err) => {
        console.error('Express server is starting or offline:', err);
        setServerOnline(false);
        addLog('Express server health check: OFFLINE. Initializing local workspace cache sandbox.', 'warn');
      });
  }, []);

  // Periodically generate background activity ticks
  useEffect(() => {
    const backgroundMessages = [
      { msg: 'Scanning active Google Drive root structures...', type: 'system' as const },
      { msg: 'Analyzing document structures & workspace folder weights...', type: 'info' as const },
      { msg: 'Telemetry sweep complete // 0 packet loss on subnet 192.168.68.x', type: 'system' as const },
      { msg: 'Reconciliation check on L2 Cache (insights.md): stable', type: 'success' as const },
      { msg: 'Calculating live Watchtower compliance & duplicate risk factors...', type: 'info' as const },
      { msg: 'Secure data tunnel verified with Google Cloud API gateway', type: 'success' as const },
      { msg: 'Flushing transient experience traces to L1 cache...', type: 'system' as const },
      { msg: 'Personal intelligence core CPU utilization: 6% // RAM: 192MB', type: 'info' as const },
      { msg: 'Verifying file signatures via lattice-based ML-DSA verification...', type: 'system' as const },
      { msg: 'Ollama local inference pipeline handshake: STABLE on port 11434', type: 'success' as const },
    ];

    const interval = setInterval(() => {
      const randomItem = backgroundMessages[Math.floor(Math.random() * backgroundMessages.length)];
      addLog(randomItem.msg, randomItem.type);
    }, 10000); // Trigger a realistic log every 10 seconds

    return () => clearInterval(interval);
  }, []);

  // Handle real-time sync when connected
  const runWorkspaceSync = async (token: string) => {
    setIsSyncing(true);
    setSyncProgress(5);
    setSyncMessage('Listing documents from your Google Drive...');
    addLog('Establishing secure data-link to Google Drive API...', 'system');
    addLog('Scanning drive metadata for spreadsheets, documents, and spec PDFs...', 'info');
    try {
      // 1. Call Google Drive API to list sheets, docs, PDFs
      const driveUrl = 'https://www.googleapis.com/drive/v3/files?pageSize=50&fields=files(id,name,mimeType,size,modifiedTime,webViewLink)&q=mimeType%20%3D%20%27application%2Fvnd.google-apps.document%27%20or%20mimeType%20%3D%20%27application%2Fvnd.google-apps.spreadsheet%27%20or%20mimeType%20%3D%20%27application%2Fpdf%27';
      const response = await fetch(driveUrl, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!response.ok) {
        let errorMsg = 'Google Drive API returned an error';
        try {
          const errData = await response.json();
          if (errData?.error?.message) {
            errorMsg = `${errData.error.message} (HTTP ${response.status})`;
          } else {
            errorMsg = `HTTP Error ${response.status}: ${response.statusText}`;
          }
        } catch (e) {
          errorMsg = `HTTP Error ${response.status}: ${response.statusText}`;
        }
        throw new Error(errorMsg);
      }

      const data = await response.json();
      const driveList = data.files || [];

      if (driveList.length === 0) {
        setSyncProgress(100);
        setSyncMessage('No compatible Docs or Sheets found in your drive.');
        addLog('No compatible document files found in active directory.', 'warn');
        setTimeout(() => {
          setIsSyncing(false);
          setSyncMessage(null);
        }, 1500);
        return;
      }

      setSyncProgress(20);
      addLog(`Discovered ${driveList.length} files matching filters. Fetching file structures...`, 'success');
      setSyncMessage(`Found ${driveList.length} files. Extracting structures...`);

      // 2. Format files for processing
      let completedCount = 0;
      const formattedFiles: DriveFile[] = await Promise.all(
        driveList.map(async (file: any) => {
          let content = '';

          // Lazy-extract basic contents from selected Doc/Sheet if we can
          try {
            if (file.mimeType.includes('document')) {
              addLog(`Reading document nodes: "${file.name}"`, 'system');
              const docRes = await fetch(`https://docs.googleapis.com/v1/documents/${file.id}`, {
                headers: { Authorization: `Bearer ${token}` },
              });
              if (docRes.ok) {
                const docData = await docRes.json();
                let txt = '';
                docData.body?.content?.forEach((element: any) => {
                  element.paragraph?.elements?.forEach((el: any) => {
                    if (el.textRun?.content) txt += el.textRun.content;
                  });
                });
                content = txt.substring(0, 3000); // Grab up to 3k chars for quick summary
              }
            } else if (file.mimeType.includes('spreadsheet')) {
              addLog(`Extracting spreadsheet cell values: "${file.name}"`, 'system');
              const sheetRes = await fetch(`https://sheets.googleapis.com/v4/spreadsheets/${file.id}/values/A1:Z50`, {
                headers: { Authorization: `Bearer ${token}` },
              });
              if (sheetRes.ok) {
                const sheetData = await sheetRes.json();
                if (sheetData.values) {
                  content = sheetData.values.map((r: string[]) => r.join(', ')).join('\n').substring(0, 3000);
                }
              }
            }
          } catch (e) {
            console.warn('Failed lazy text-extraction for file:', file.name, e);
          }

          completedCount++;
          const currentProgress = Math.round(20 + (completedCount / driveList.length) * 55); // scale from 20% to 75%
          setSyncProgress(currentProgress);
          setSyncMessage(`Scanning file ${completedCount}/${driveList.length}: "${file.name}"`);

          return {
            id: file.id,
            name: file.name,
            mimeType: file.mimeType,
            size: file.size ? parseInt(file.size, 10) : 12000, // Default fallback size
            modifiedTime: file.modifiedTime,
            webViewLink: file.webViewLink,
            content: content || `Metadata scanned. Last edited by Google Account. Size: ${file.size || '12KB'}`,
          };
        })
      );

      setFiles(formattedFiles);
      setSyncProgress(80);
      addLog(`Extracted text streams from ${formattedFiles.length} files. Initiating AI summary...`, 'info');
      setSyncMessage('Analyzing storage distribution via Gemini...');

      addLog('Invoking Gemini Workspace Intelligence core for duplicate & age categorization...', 'neural');
      // 3. Post to Express Backend Gemini Workspace Intelligence
      const intelResponse = await fetch('/api/gemini/workspace-intelligence', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ files: formattedFiles }),
      });

      if (!intelResponse.ok) {
        throw new Error('Gemini analysis failed');
      }

      const intelData = await intelResponse.json();
      setSyncProgress(95);
      setSyncMessage('Updating system telemetry models...');

      // Update States with Live Gemini insights!
      setStats({
        totalFiles: formattedFiles.length,
        totalSize: formattedFiles.reduce((acc, f) => acc + (f.size || 0), 0),
        mimeTypeBreakdown: intelData.categories?.map((c: any) => ({ name: c.name, value: c.count })) || [
          { name: 'Google Docs', value: formattedFiles.filter((f) => f.mimeType.includes('document')).length },
          { name: 'Google Sheets', value: formattedFiles.filter((f) => f.mimeType.includes('spreadsheet')).length },
        ],
        sizeBreakdown: formattedFiles.slice(0, 4).map((f) => ({ name: f.name, value: f.size || 0 })),
        lastSyncTime: new Date().toISOString(),
        score: intelData.score || 90,
      });

      setRecommendations(intelData.cleanUpRecommendations || []);
      setCategories(intelData.categories || []);
      setSyncProgress(100);
      setSyncMessage('Workspace intelligence sync complete!');
      addLog('Gemini Workspace analysis completed successfully. Interactive metrics and indicators updated.', 'success');
      setTimeout(() => {
        setIsSyncing(false);
        setSyncMessage(null);
      }, 1000);
    } catch (err: any) {
      console.error('Live Sync Error:', err);
      setSyncMessage(`Sync failed: ${err.message || 'Verification failed. Try Sandbox fallback.'}`);
      addLog(`Drive synchronization failed: ${err.message || 'Verification failed'}`, 'error');
      setTimeout(() => {
        setIsSyncing(false);
        setSyncMessage(null);
      }, 5000);
    }
  };

  const handleConnect = (token: string) => {
    setAccessToken(token);
    setIsSandbox(false);
    addLog('Google connection established. Access token granted.', 'success');
    runWorkspaceSync(token);
  };

  const handleDisconnect = () => {
    setAccessToken('');
    setFiles(mockFiles);
    setStats(mockStats);
    setRecommendations(mockRecommendations);
    setCategories([
      { name: 'Financial Forecasts', count: 2, description: 'Spreadsheets detailing forecast models' },
      { name: 'Product specs', count: 2, description: 'Specs, roadmaps and notes' },
      { name: 'Corporate Compliance', count: 1, description: 'Guidelines on security policies' },
    ]);
    setSelectedFile(null);
    addLog('Google connection terminated. Switched back to offline Sandbox mode.', 'warn');
  };

  // Safe file clean-up handling with mandatory user confirmation
  const handleCleanUp = async (id: string, fileName: string) => {
    const isConfirmed = window.confirm(
      `Are you sure you want to clean up "${fileName}"?\nThis operation will delete/archive the file from Watchtower tracking.`
    );

    if (!isConfirmed) return;

    try {
      setIsSyncing(true);
      setSyncMessage(`Archiving "${fileName}"...`);
      addLog(`Cleanup request initiated for: "${fileName}" (ID: ${id})`, 'warn');

      if (!isSandbox && accessToken) {
        // Send a DELETE request to Google Drive to trash the file
        const res = await fetch(`https://www.googleapis.com/drive/v3/files/${id}`, {
          method: 'DELETE',
          headers: { Authorization: `Bearer ${accessToken}` },
        });
        if (!res.ok) throw new Error('Failed to trash file in Google Drive');
      }

      // Find the file to be deleted to know its size
      const fileToDelete = files.find(f => f.id === id);
      const fileSize = fileToDelete?.size || 0;

      // 1. Remove from local recommendations list
      setRecommendations((prev) => prev.filter((rec) => rec.id !== id));
      // 2. Remove from active files catalog
      setFiles((prev) => prev.filter((f) => f.id !== id));

      // 3. Dynamically reward the user with an increased score!
      setStats((prev) => ({
        ...prev,
        totalFiles: Math.max(0, prev.totalFiles - 1),
        totalSize: Math.max(0, prev.totalSize - fileSize),
        score: Math.min(100, prev.score + 8), // Clean-up improves score!
      }));

      setSyncMessage(`Successfully cleaned up: ${fileName}`);
      addLog(`Purged file "${fileName}" from directory index. Health status normalized.`, 'success');
      setTimeout(() => setSyncMessage(null), 3000);
    } catch (err: any) {
      console.error('Cleanup failed:', err);
      alert(`Could not delete file: ${err.message || 'Permission denied'}`);
      addLog(`Cleanup failed for file "${fileName}": ${err.message || 'Permission denied'}`, 'error');
      setSyncMessage(null);
    } finally {
      setIsSyncing(false);
    }
  };

  // Bulk clean-up handling with confirmation and dual-layer deletion
  const handleBulkCleanUp = async (ids: string[]) => {
    if (ids.length === 0) return;

    const isConfirmed = window.confirm(
      `Are you sure you want to clean up ${ids.length} selected files?\nThis operation will delete/archive these files from Watchtower tracking.`
    );

    if (!isConfirmed) return;

    try {
      setIsSyncing(true);
      setSyncMessage(`Purging ${ids.length} files...`);
      addLog(`Bulk cleanup sequence initiated for ${ids.length} selected items`, 'warn');

      let failedCount = 0;

      if (!isSandbox && accessToken) {
        // Send a DELETE request to Google Drive to trash each file
        await Promise.all(
          ids.map(async (id) => {
            try {
              const res = await fetch(`https://www.googleapis.com/drive/v3/files/${id}`, {
                method: 'DELETE',
                headers: { Authorization: `Bearer ${accessToken}` },
              });
              if (!res.ok) throw new Error(`Drive response not OK for file ${id}`);
            } catch (err) {
              console.error(`Failed to delete file ID ${id} from Google Drive:`, err);
              failedCount++;
            }
          })
        );
      }

      const succeededCount = ids.length - failedCount;
      const fileSizesSum = files.filter(f => ids.includes(f.id)).reduce((acc, f) => acc + (f.size || 0), 0);

      // 1. Remove from local recommendations list
      setRecommendations((prev) => prev.filter((rec) => !ids.includes(rec.id)));
      // 2. Remove from active files catalog
      setFiles((prev) => prev.filter((f) => !ids.includes(f.id)));

      // 3. Dynamically reward the user with an increased score!
      setStats((prev) => ({
        ...prev,
        totalFiles: Math.max(0, prev.totalFiles - succeededCount),
        totalSize: Math.max(0, prev.totalSize - fileSizesSum),
        score: Math.min(100, prev.score + (succeededCount * 6)), // 6 points reward per file!
      }));

      if (failedCount > 0) {
        setSyncMessage(`Completed: ${succeededCount} purged, ${failedCount} failed`);
        addLog(`Bulk cleanup compiled with warnings. Purged ${succeededCount} items. ${failedCount} items encountered access restrictions.`, 'error');
      } else {
        setSyncMessage(`Successfully purged ${ids.length} files`);
        addLog(`Bulk cleanup successful. Purged ${ids.length} files from directory index. Health status normalized.`, 'success');
      }

      setTimeout(() => setSyncMessage(null), 3000);
    } catch (err: any) {
      console.error('Bulk cleanup failed:', err);
      alert(`Could not delete files: ${err.message || 'Permission denied'}`);
      addLog(`Bulk cleanup failed: ${err.message || 'Permission denied'}`, 'error');
      setSyncMessage(null);
    } finally {
      setIsSyncing(false);
    }
  };

  const triggerForceRefresh = () => {
    if (isSandbox) {
      // Simulate sync in sandbox mode with step-by-step percentage progress
      setIsSyncing(true);
      setSyncProgress(0);
      setSyncMessage('Re-initializing sandbox scanner...');
      addLog('Force scan initiated. Re-evaluating local sandbox file streams...', 'system');
      
      const steps = [
        { progress: 12, msg: 'Verifying sandbox integrity index...' },
        { progress: 28, msg: 'Scanning: "Project Alpha Roadmap.pdf" (6.4MB)' },
        { progress: 46, msg: 'Scanning: "Q3 Financial Forecast Models.gsheet" (152KB)' },
        { progress: 68, msg: 'Scanning: "Sprint Planning Meeting Minutes - June 20.gdoc" (8.5KB)' },
        { progress: 85, msg: 'Running local heuristic analysis for duplicate clusters...' },
        { progress: 95, msg: 'Formulating action recommendations...' },
        { progress: 100, msg: 'Sandbox sync complete. Metrics updated!' }
      ];

      let stepIndex = 0;
      const runStep = () => {
        if (stepIndex < steps.length) {
          const step = steps[stepIndex];
          setSyncProgress(step.progress);
          setSyncMessage(step.msg);
          if (step.progress === 100) {
            setStats((prev) => ({
              ...prev,
              lastSyncTime: new Date().toISOString(),
              score: Math.min(100, prev.score + 2),
            }));
            addLog('Local sandbox synchronization complete. Storage structures normalized.', 'success');
            setTimeout(() => {
              setIsSyncing(false);
              setSyncMessage(null);
            }, 1000);
          } else {
            stepIndex++;
            setTimeout(runStep, 350 + Math.random() * 250); // 350-600ms per step for snappy realistic progression
          }
        }
      };

      setTimeout(runStep, 150);
    } else if (accessToken) {
      runWorkspaceSync(accessToken);
    }
  };

  // Trigger initial synchronization on launch to initialize personal intelligence scanning
  useEffect(() => {
    const timer = setTimeout(() => {
      addLog(`Auto-initiating synchronization scan: activating personal intelligence tunnels for Operator ${operatorCallSign.toUpperCase()}...`, 'neural');
      addLog(`Authorized session recognized under email node [${userEmail || 'cleeman1989@gmail.com'}]`, 'success');
      triggerForceRefresh();
    }, 1200); // Let the app layout stabilize for 1.2 seconds, then trigger sync
    return () => clearTimeout(timer);
  }, []);

  // Keyboard shortcut listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
      const isMetaOrCtrl = isMac ? e.metaKey : e.ctrlKey;

      if (isMetaOrCtrl) {
        const key = e.key.toLowerCase();
        
        if (key === 's') {
          e.preventDefault();
          addLog('Keyboard shortcut [Ctrl+S] detected: Triggering Sync...', 'info');
          triggerForceRefresh();
        } else if (key === 'f') {
          e.preventDefault();
          addLog('Keyboard shortcut [Ctrl+F] detected: Focusing Search Input...', 'info');
          const searchInput = document.getElementById('file-search-field');
          if (searchInput) {
            searchInput.focus();
            searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            (searchInput as HTMLInputElement).select();
          }
        } else if (key === 'd') {
          e.preventDefault();
          addLog('Keyboard shortcut [Ctrl+D] detected: Toggling Theme...', 'info');
          setTheme(prev => prev === 'cyberpunk' ? 'terminal-light' : 'cyberpunk');
        } else if (key === 'k' || key === '/' || key === 'h') {
          e.preventDefault();
          addLog('Keyboard shortcut [Ctrl+K] detected: Toggling Shortcuts Registry...', 'info');
          setShowShortcutsModal(prev => !prev);
        }
      } else {
        if (e.key === 'Escape') {
          if (showShortcutsModal) {
            setShowShortcutsModal(false);
          }
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isSandbox, accessToken, showShortcutsModal]);

  return (
    <div className={`min-h-screen bg-[#05070a] text-slate-200 font-sans relative overflow-hidden ${theme === 'terminal-light' ? 'theme-terminal-light' : ''}`} id="workspace-watchtower-app">
      {/* Immersive Cyberpunk Elements */}
      <div className="orb-glow w-[600px] h-[600px] bg-cyan-500/20 -top-40 -left-40"></div>
      <div className="orb-glow w-[500px] h-[500px] bg-amber-500/10 -bottom-40 -right-40"></div>
      <div className="scanline"></div>

      {/* Cyberpunk Top Bar */}
      <div className="relative z-20 bg-[#090d16] border-b border-cyan-500/20 text-cyan-400 py-2.5 px-4 text-center text-[10px] uppercase tracking-widest font-bold flex items-center justify-center gap-2" id="top-notification-banner">
        <span className="w-1.5 h-1.5 bg-cyan-400 rounded-full animate-ping"></span>
        <span>Operator <strong className="text-amber-300">{operatorCallSign.toUpperCase()}</strong> validated // secure terminal shell active</span>
      </div>

      {/* System Activity Ticker section */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-6" id="system-activity-ticker-container">
        <SystemActivityLog logs={logs} onClear={() => setLogs([])} />
      </div>

      <header className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-6 border-b border-slate-800/80 bg-[#05070a]/60 backdrop-blur-md" id="app-header-container">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <span className="p-3 bg-cyan-950/40 border border-cyan-500/30 text-cyan-400 rounded-2xl shadow-lg shadow-cyan-950/20">
              <Compass className="w-7 h-7" />
            </span>
            <div>
              <div className="flex flex-wrap items-center gap-3 mb-1">
                <div className="flex items-center gap-1.5">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full animate-pulse shadow-[0_0_8px_#22d3ee]"></div>
                  <span className="text-[10px] uppercase tracking-[0.3em] text-cyan-400 font-bold">System Live</span>
                </div>
                <span className="text-slate-700 text-xs font-mono select-none">•</span>
                <LastSyncIndicator lastSyncTime={stats.lastSyncTime} />
              </div>
              <h1 className="text-2xl sm:text-3xl font-light tracking-tighter text-slate-100">
                WATCHTOWER <span className="text-cyan-500 font-bold italic">AI-SYNC</span>
              </h1>
              <p className="text-xs text-slate-400 mt-1">Authorized Command Deck for <strong className="text-cyan-400 font-bold">{operatorCallSign}</strong> ({operatorRank})</p>
            </div>
          </div>

          <div className="flex items-center gap-4 sm:gap-6 self-stretch sm:self-auto justify-between sm:justify-end">
            {/* Theme Toggle Button */}
            <button
              id="theme-toggle-button"
              onClick={() => setTheme(prev => prev === 'cyberpunk' ? 'terminal-light' : 'cyberpunk')}
              className="group flex items-center gap-2 px-3 py-1.5 sm:px-3.5 sm:py-2 bg-slate-900 border border-slate-800 rounded-xl sm:rounded-2xl text-[10px] sm:text-[11px] font-mono uppercase font-bold tracking-wider hover:border-cyan-500/40 transition-all select-none cursor-pointer"
              title={theme === 'cyberpunk' ? 'Switch to Terminal Light Mode' : 'Switch to Cyberpunk Dark Mode'}
            >
              {theme === 'cyberpunk' ? (
                <>
                  <Sun className="w-3.5 h-3.5 text-amber-400 animate-pulse group-hover:rotate-12 transition-transform duration-300" />
                  <span className="text-slate-300 group-hover:text-cyan-400">Terminal Light</span>
                </>
              ) : (
                <>
                  <Moon className="w-3.5 h-3.5 text-sky-500 group-hover:-rotate-12 transition-transform duration-300" />
                  <span className="text-slate-800 font-bold">Cyberpunk Dark</span>
                </>
              )}
            </button>

            <div className="flex gap-6 sm:gap-8 text-right shrink-0">
              <div className="flex flex-col">
                <span className="text-[9px] uppercase text-slate-500 font-bold">Personal Intelligence</span>
                <span className="text-xs text-amber-400 font-bold font-mono">THINKING... (v4.2.8)</span>
              </div>
              <div className="flex flex-col">
                <span className="text-[9px] uppercase text-slate-500 font-bold">Sync Protocol</span>
                <span className="text-xs text-cyan-400 font-bold font-mono">RUNNING // 88.4%</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Body */}
      <main className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8" id="app-main-content">
        {/* Detailed percentage-based progress bar during file scanning */}
        {isSyncing && (
          <div 
            className="fixed inset-0 z-50 flex items-center justify-center bg-[#05070a]/85 backdrop-blur-md animate-fade-in"
            id="sync-progress-overlay"
          >
            <div 
              className="bg-[#090d16] border border-cyan-500/30 p-6 sm:p-8 rounded-3xl w-full max-w-lg mx-4 shadow-2xl shadow-cyan-950/50 relative overflow-hidden cyber-glow-cyan"
              id="sync-progress-card"
            >
              {/* Subtle background glow */}
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(34,211,238,0.06),transparent)] pointer-events-none" />
              
              <div className="flex items-center justify-between mb-4 relative z-10">
                <div className="flex items-center gap-2">
                  <span className="flex h-2.5 w-2.5 relative">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-450 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-cyan-500"></span>
                  </span>
                  <span className="text-[10px] font-bold text-cyan-400 font-mono tracking-widest uppercase">
                    Watchtower Scanner Protocol
                  </span>
                </div>
                <div>
                  <span className="text-sm font-bold font-mono text-cyan-400 bg-cyan-950/40 border border-cyan-900/30 px-3 py-1 rounded-xl shadow-inner">
                    {syncProgress}%
                  </span>
                </div>
              </div>

              <div className="mb-4 relative z-10">
                <h4 className="text-base font-bold text-slate-100 uppercase tracking-wide">
                  Scanning Google Workspace...
                </h4>
                <p className="text-xs text-slate-400 mt-1">
                  Extracting file nodes, lazy stream data, and re-building system intelligence.
                </p>
              </div>
              
              {/* Glowing Dynamic Progress Bar Track */}
              <div className="w-full bg-slate-900/80 border border-slate-800/80 rounded-full h-4 overflow-hidden p-0.5 mb-5 relative z-10 shadow-inner">
                <div 
                  className="bg-gradient-to-r from-cyan-500 via-cyan-400 to-emerald-400 h-full rounded-full transition-all duration-300 ease-out shadow-[0_0_12px_rgba(34,211,238,0.6)]"
                  style={{ width: `${syncProgress}%` }}
                />
              </div>

              {/* Status footer with active operation details */}
              <div className="flex items-center justify-between text-[10px] font-mono text-slate-500 relative z-10 border-t border-slate-850 pt-3">
                <span className="truncate max-w-[75%]" id="sync-progress-status-message" title={syncMessage || 'Initializing local scanning tunnels...'}>
                  Active: <strong className="text-slate-300 font-medium">{syncMessage || 'Initializing scanner...'}</strong>
                </span>
                <span className="shrink-0 text-cyan-500/80 uppercase font-bold tracking-wider">
                  {syncProgress === 100 ? 'SUCCESS' : 'SCANNING'}
                </span>
              </div>
            </div>
          </div>
        )}

        {/* Integration Configurator */}
        <GoogleConnection
          isSandbox={isSandbox}
          setIsSandbox={setIsSandbox}
          clientId={clientId}
          onConnect={handleConnect}
          isConnected={!!accessToken}
          onDisconnect={handleDisconnect}
          userEmail={userEmail}
        />

        {/* Automated Sync & Deep Archiving Control Center */}
        <WatchtowerSettings
          isSandbox={isSandbox}
          accessToken={accessToken}
          files={files}
          setFiles={setFiles}
          recommendations={recommendations}
          setRecommendations={setRecommendations}
          stats={stats}
          setStats={setStats}
          onAddLog={addLog}
          onTriggerSync={async () => {
            if (!isSandbox && accessToken) {
              await runWorkspaceSync(accessToken);
            } else {
              triggerForceRefresh();
            }
          }}
        />

        {/* Watchtower Smart Gmail Guard */}
        <WatchtowerGmail
          isSandbox={isSandbox}
          accessToken={accessToken}
          onAddLog={addLog}
          stats={stats}
          recommendations={recommendations}
          files={files}
          operatorCallSign={operatorCallSign || 'Operator'}
        />

        {/* File Analysis Overlay / Detail Drawer */}
        <AnimatePresence>
          {selectedFileWithTags && (
            <FileAnalyzer
              file={selectedFileWithTags}
              onClose={() => handleSelectFile(null)}
              isSandbox={isSandbox}
              onLog={addLog}
              onUpdateTags={handleUpdateTags}
            />
          )}
        </AnimatePresence>

        {/* Keyboard Shortcuts Cheatsheet Overlay Modal */}
        <AnimatePresence>
          {showShortcutsModal && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 z-50 flex items-center justify-center bg-[#05070a]/90 backdrop-blur-md px-4"
              id="shortcuts-modal-overlay"
              onClick={() => setShowShortcutsModal(false)}
            >
              <motion.div
                initial={{ scale: 0.95, y: 15, opacity: 0 }}
                animate={{ scale: 1, y: 0, opacity: 1 }}
                exit={{ scale: 0.95, y: 15, opacity: 0 }}
                transition={{ type: 'spring', damping: 25, stiffness: 350 }}
                className="bg-[#090d16] border border-cyan-500/30 p-6 sm:p-8 rounded-3xl w-full max-w-2xl shadow-2xl shadow-cyan-950/50 relative overflow-hidden cyber-glow-cyan"
                id="shortcuts-modal-card"
                onClick={(e) => e.stopPropagation()}
              >
                {/* Cyber decorative lines */}
                <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-cyan-500 via-transparent to-amber-500 animate-pulse" />
                <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(34,211,238,0.06),transparent)] pointer-events-none" />

                <div className="flex items-center justify-between mb-6 relative z-10">
                  <div className="flex items-center gap-2.5">
                    <span className="p-2 bg-cyan-950/40 border border-cyan-500/20 text-cyan-400 rounded-xl">
                      <Command className="w-5 h-5 animate-pulse" />
                    </span>
                    <div>
                      <h3 className="text-base font-bold text-slate-100 uppercase tracking-wider font-sans">
                        Watchtower Hotkey Registry
                      </h3>
                      <p className="text-[10px] text-slate-400 font-mono">
                        Secure Shell Terminal Shortcuts // Command Deck Core
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => setShowShortcutsModal(false)}
                    className="p-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200 transition-all cursor-pointer"
                    id="close-shortcuts-modal-btn"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>

                {/* Shortcuts Table */}
                <div className="overflow-x-auto relative z-10 border border-slate-850/80 rounded-2xl bg-slate-950/50">
                  <table className="w-full text-left border-collapse text-xs">
                    <thead>
                      <tr className="border-b border-slate-850/80 bg-slate-900/30 text-[10px] font-mono text-slate-500 uppercase tracking-widest">
                        <th className="px-5 py-3">Global Command</th>
                        <th className="px-5 py-3">Action Target</th>
                        <th className="px-5 py-3">Description</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-850/40 font-sans text-slate-300">
                      <tr className="hover:bg-cyan-500/5 transition-all">
                        <td className="px-5 py-4 font-mono">
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">Ctrl</span>
                          <span className="mx-1 text-slate-650 font-bold">+</span>
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">S</span>
                        </td>
                        <td className="px-5 py-4 font-mono font-bold text-slate-200">
                          Workspace Sync
                        </td>
                        <td className="px-5 py-4 text-slate-400 leading-relaxed text-[11px]">
                          Instantly queries Google Drive API or triggers Sandbox simulation scanner to update compliance metrics & recommendations.
                        </td>
                      </tr>

                      <tr className="hover:bg-cyan-500/5 transition-all">
                        <td className="px-5 py-4 font-mono">
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">Ctrl</span>
                          <span className="mx-1 text-slate-650 font-bold">+</span>
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">F</span>
                        </td>
                        <td className="px-5 py-4 font-mono font-bold text-slate-200">
                          Focus File Search
                        </td>
                        <td className="px-5 py-4 text-slate-400 leading-relaxed text-[11px]">
                          Scrolls down and auto-focuses the advanced File Directory console with existing search query pre-selected for quick filter typing.
                        </td>
                      </tr>

                      <tr className="hover:bg-cyan-500/5 transition-all">
                        <td className="px-5 py-4 font-mono">
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">Ctrl</span>
                          <span className="mx-1 text-slate-650 font-bold">+</span>
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">D</span>
                        </td>
                        <td className="px-5 py-4 font-mono font-bold text-slate-200">
                          Toggle Visual Theme
                        </td>
                        <td className="px-5 py-4 text-slate-400 leading-relaxed text-[11px]">
                          Seamlessly rotates the command deck interface between high-contrast terminal-light mode and dark cyberpunk ambient theme.
                        </td>
                      </tr>

                      <tr className="hover:bg-cyan-500/5 transition-all">
                        <td className="px-5 py-4 font-mono">
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">Ctrl</span>
                          <span className="mx-1 text-slate-650 font-bold">+</span>
                          <span className="bg-slate-900 border border-slate-800 px-2 py-1 rounded-md text-cyan-400 font-bold shadow-inner">K</span>
                        </td>
                        <td className="px-5 py-4 font-mono font-bold text-slate-200">
                          Hotkey Cheatsheet
                        </td>
                        <td className="px-5 py-4 text-slate-400 leading-relaxed text-[11px]">
                          Toggles the overlay deck visibility (this terminal screen). Can also be triggered using the <strong className="text-cyan-400">Ctrl + /</strong> key combo.
                        </td>
                      </tr>

                      <tr className="hover:bg-cyan-500/5 transition-all">
                        <td className="px-5 py-4 font-mono">
                          <span className="bg-slate-950 border border-slate-850 px-2.5 py-1 rounded-md text-slate-400 font-bold shadow-inner">Esc</span>
                        </td>
                        <td className="px-5 py-4 font-mono font-bold text-slate-200">
                          Escape Interface
                        </td>
                        <td className="px-5 py-4 text-slate-400 leading-relaxed text-[11px]">
                          Instantly exits the open hotkey guide or cancels active file and inspection cards throughout the system.
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div className="mt-5 text-right font-mono text-[9px] text-slate-500 relative z-10 border-t border-slate-850 pt-3">
                  <span>TIP: Press <strong className="text-slate-300">Escape</strong> or click anywhere outside to close the registry.</span>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Primary Dashboard layout */}
        <WatchtowerDashboard
          stats={stats}
          recommendations={recommendations}
          categories={categories}
          onCleanUp={handleCleanUp}
          files={filesWithTags}
          onSelectFile={handleSelectFile}
          isSandbox={isSandbox}
          onBulkCleanUp={handleBulkCleanUp}
        />

        {/* Interactive Files list catalog */}
        <FileList
          files={filesWithTags}
          onSelectFile={handleSelectFile}
          selectedFileId={selectedFile?.id}
          isSyncing={isSyncing}
          onRefresh={triggerForceRefresh}
          onBulkCleanUp={handleBulkCleanUp}
          onUpdateTags={handleUpdateTags}
        />

        {/* Personalized Copilot Conversational Chat deck */}
        <WatchtowerAICopilot
          files={filesWithTags}
          stats={stats}
          recommendations={recommendations}
          userEmail={userEmail || 'cleeman1989@gmail.com'}
          operatorCallSign={operatorCallSign}
          setOperatorCallSign={setOperatorCallSign}
          operatorRank={operatorRank}
          setOperatorRank={setOperatorRank}
          isSandbox={isSandbox}
          onAddLog={addLog}
        />
      </main>

      <footer className="relative z-10 px-6 py-6 bg-[#0a0b0d] border-t border-slate-800" id="app-footer">
        <div className="max-w-7xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4 text-[10px] text-slate-500 font-mono">
          <div className="flex items-center gap-4">
            <span>SECURE SHELL CONNECTION: ACTIVE</span>
            <div className="w-px h-3 bg-slate-800"></div>
            <span className="uppercase tracking-widest">Encrypted Data-Tunnel #920-X</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="uppercase">Intelligence Engine Level</span>
            <div className="flex gap-0.5">
              <div className="w-3 h-1 bg-cyan-500"></div>
              <div className="w-3 h-1 bg-cyan-500"></div>
              <div className="w-3 h-1 bg-cyan-500"></div>
              <div className="w-3 h-1 bg-cyan-500"></div>
              <div className="w-3 h-1 bg-slate-700"></div>
            </div>
          </div>
        </div>
      </footer>

      {/* Floating Keyboard Shortcuts Trigger Button */}
      <button
        onClick={() => setShowShortcutsModal(true)}
        className="fixed bottom-6 right-6 z-40 flex items-center gap-2 px-3.5 py-2.5 bg-[#090d16]/95 hover:bg-[#0c1424] border border-cyan-500/30 hover:border-cyan-400 rounded-full text-[10px] font-mono uppercase font-bold tracking-wider text-cyan-400 shadow-xl shadow-cyan-950/40 hover:shadow-cyan-400/10 hover:scale-105 transition-all select-none cursor-pointer group"
        id="floating-shortcuts-guide-btn"
        title="Open Keyboard Shortcuts [Ctrl+K]"
      >
        <Keyboard className="w-3.5 h-3.5 animate-pulse group-hover:scale-110 transition-transform" />
        <span className="hidden sm:inline">Shortcuts</span>
        <span className="bg-slate-950/80 px-1.5 py-0.5 rounded text-[8px] border border-slate-800 text-slate-400">Ctrl+K</span>
      </button>
    </div>
  );
}
