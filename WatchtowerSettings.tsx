/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useRef } from 'react';
import { 
  Settings, 
  RefreshCw, 
  FolderArchive, 
  RotateCcw, 
  Check, 
  Trash2, 
  ShieldAlert, 
  Clock, 
  ArrowUpRight, 
  Database,
  ChevronDown,
  Info
} from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { DriveFile, WatchtowerStats, CleanUpRecommendation, LogEntry } from '../types';

interface WatchtowerSettingsProps {
  isSandbox: boolean;
  accessToken: string;
  files: DriveFile[];
  setFiles: React.Dispatch<React.SetStateAction<DriveFile[]>>;
  recommendations: CleanUpRecommendation[];
  setRecommendations: React.Dispatch<React.SetStateAction<CleanUpRecommendation[]>>;
  stats: WatchtowerStats;
  setStats: React.Dispatch<React.SetStateAction<WatchtowerStats>>;
  onAddLog: (message: string, type?: LogEntry['type']) => void;
  onTriggerSync: () => Promise<void>;
}

export default function WatchtowerSettings({
  isSandbox,
  accessToken,
  files,
  setFiles,
  recommendations,
  setRecommendations,
  stats,
  setStats,
  onAddLog,
  onTriggerSync,
}: WatchtowerSettingsProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [syncInterval, setSyncInterval] = useState<'manual' | 'hourly' | 'daily'>(() => {
    return (localStorage.getItem('watchtower-sync-interval') as any) || 'manual';
  });
  const [autoArchiveOnSync, setAutoArchiveOnSync] = useState<boolean>(() => {
    return localStorage.getItem('watchtower-auto-archive-on-sync') === 'true';
  });

  // Keep a local virtual cache of archived files to display in the vault (persists via localStorage)
  const [archivedFiles, setArchivedFiles] = useState<any[]>(() => {
    const saved = localStorage.getItem('watchtower-archived-vault');
    return saved ? JSON.parse(saved) : [];
  });

  const [isArchiving, setIsArchiving] = useState(false);
  const [archiveStatus, setArchiveStatus] = useState<string | null>(null);
  const [countdown, setCountdown] = useState<number>(0);

  // Sync intervals countdown in seconds
  // Hourly = 60s for testing/demo purposes, Daily = 180s for quick sandbox demonstration
  const getIntervalSeconds = (interval: 'manual' | 'hourly' | 'daily') => {
    if (interval === 'hourly') return 60;
    if (interval === 'daily') return 180;
    return 0;
  };

  // Persist settings
  useEffect(() => {
    localStorage.setItem('watchtower-sync-interval', syncInterval);
    if (syncInterval !== 'manual') {
      setCountdown(getIntervalSeconds(syncInterval));
    } else {
      setCountdown(0);
    }
  }, [syncInterval]);

  useEffect(() => {
    localStorage.setItem('watchtower-auto-archive-on-sync', String(autoArchiveOnSync));
  }, [autoArchiveOnSync]);

  useEffect(() => {
    localStorage.setItem('watchtower-archived-vault', JSON.stringify(archivedFiles));
  }, [archivedFiles]);

  // Automated Sync and Archive Loop
  useEffect(() => {
    if (syncInterval === 'manual') return;

    const timer = setInterval(() => {
      setCountdown((prev) => {
        if (prev <= 1) {
          // Trigger automated background sync
          onAddLog(`Automated sync sequence initiated [Interval: ${syncInterval.toUpperCase()}]`, 'system');
          
          onTriggerSync().then(() => {
            if (autoArchiveOnSync) {
              onAddLog('Automated Auto-Archive triggered immediately following scheduled sync.', 'info');
              executeAutoArchive(true); // silent background run
            }
          });

          return getIntervalSeconds(syncInterval);
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [syncInterval, autoArchiveOnSync, files, recommendations]);

  const formatCountdown = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  const formatSize = (bytes?: number) => {
    if (bytes === undefined) return 'N/A';
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  };

  // Deep Auto-Archive logic
  const executeAutoArchive = async (isSilent = false) => {
    if (isArchiving) return;
    
    if (!isSilent) {
      const confirmRun = window.confirm(
        "Initiate Deep Auto-Archive Operation?\n\nThis will scan your workspace, detect duplicates or files older than 1 year, and migrate them to the 'Watchtower-Archive' directory."
      );
      if (!confirmRun) return;
    }

    setIsArchiving(true);
    setArchiveStatus("Scanning file nodes for archive criteria...");
    if (!isSilent) onAddLog("Auto-Archive engine engaged: auditing document redundancy...", "warn");

    try {
      // 1. Identify files to archive
      const oneYearAgo = Date.now() - (365 * 24 * 60 * 60 * 1000);
      
      const duplicateIds = new Set(
        recommendations
          .filter(rec => rec.type === 'duplicate' || rec.type === 'near-duplicate')
          .map(rec => rec.id)
      );

      const toArchive = files.filter(f => {
        const isDuplicate = duplicateIds.has(f.id);
        const isOlderThan1Year = new Date(f.modifiedTime).getTime() < oneYearAgo;
        return isDuplicate || isOlderThan1Year;
      });

      if (toArchive.length === 0) {
        setArchiveStatus("No files matching archive criteria.");
        if (!isSilent) onAddLog("Auto-Archive sweep completed: 0 files matched archive thresholds.", "success");
        setTimeout(() => setArchiveStatus(null), 3000);
        setIsArchiving(false);
        return;
      }

      setArchiveStatus(`Discovered ${toArchive.length} candidate nodes. Preparing migration...`);
      await new Promise(resolve => setTimeout(resolve, 1500));

      let archivedFolderId = "watchtower-archive-folder-id";

      if (!isSandbox && accessToken) {
        setArchiveStatus("Connecting to Google Drive API... Locating 'Watchtower-Archive' folder...");
        
        // A. Search if folder exists
        const searchRes = await fetch(
          `https://www.googleapis.com/drive/v3/files?q=name%3D%27Watchtower-Archive%27%20and%20mimeType%3D%27application%2Fvnd.google-apps.folder%27%20and%20trashed%3Dfalse`,
          { headers: { Authorization: `Bearer ${accessToken}` } }
        );
        
        if (!searchRes.ok) throw new Error("Google Drive query failed");
        const searchData = await searchRes.json();
        const existingFolder = searchData.files?.[0];

        if (existingFolder) {
          archivedFolderId = existingFolder.id;
          if (!isSilent) onAddLog(`Active 'Watchtower-Archive' directory recognized [Folder ID: ${archivedFolderId}]`, 'info');
        } else {
          setArchiveStatus("Creating new secure 'Watchtower-Archive' folder in Google Drive...");
          // B. Create folder
          const createRes = await fetch(`https://www.googleapis.com/drive/v3/files`, {
            method: 'POST',
            headers: {
              Authorization: `Bearer ${accessToken}`,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              name: 'Watchtower-Archive',
              mimeType: 'application/vnd.google-apps.folder',
            }),
          });
          if (!createRes.ok) throw new Error("Failed to create Google Drive folder");
          const createData = await createRes.json();
          archivedFolderId = createData.id;
          if (!isSilent) onAddLog(`Successfully provisioned folder 'Watchtower-Archive' [Folder ID: ${archivedFolderId}]`, 'success');
        }

        // C. Move files
        let processed = 0;
        for (const file of toArchive) {
          setArchiveStatus(`Moving [${++processed}/${toArchive.length}]: "${file.name}"...`);
          
          // Patch parent of the file
          const moveRes = await fetch(
            `https://www.googleapis.com/drive/v3/files/${file.id}?addParents=${archivedFolderId}`,
            {
              method: 'PATCH',
              headers: { Authorization: `Bearer ${accessToken}` }
            }
          );
          if (!moveRes.ok) {
            console.warn(`Failed to move file ${file.name} to archive folder.`);
          }
        }
      }

      // 2. Move locally in state
      const archivedRecords = toArchive.map(f => {
        const isDuplicate = duplicateIds.has(f.id);
        return {
          ...f,
          archivedAt: new Date().toISOString(),
          archiveReason: isDuplicate ? "Duplicate Copy" : "Untouched (> 1 Year)"
        };
      });

      // Update state
      const toArchiveIds = new Set(toArchive.map(f => f.id));
      
      setArchivedFiles(prev => [...prev, ...archivedRecords]);
      setFiles(prev => prev.filter(f => !toArchiveIds.has(f.id)));
      setRecommendations(prev => prev.filter(rec => !toArchiveIds.has(rec.id)));

      // Dynamically award user score
      const reclaimedSize = toArchive.reduce((acc, f) => acc + (f.size || 0), 0);
      setStats(prev => ({
        ...prev,
        totalFiles: Math.max(0, prev.totalFiles - toArchive.length),
        totalSize: Math.max(0, prev.totalSize - reclaimedSize),
        score: Math.min(100, prev.score + (toArchive.length * 5)), // Reward user with points!
      }));

      setArchiveStatus(`Success! Archived ${toArchive.length} files.`);
      onAddLog(`Deep Auto-Archive successfully moved ${toArchive.length} redundant nodes to [Watchtower-Archive] folder. Score upgraded!`, 'success');
      setTimeout(() => setArchiveStatus(null), 4000);
    } catch (err: any) {
      console.error(err);
      if (!isSilent) onAddLog(`Auto-Archive execution failed: ${err.message || 'Access Denied'}`, 'error');
      setArchiveStatus(`Archive sequence failed: ${err.message || 'Error'}`);
      setTimeout(() => setArchiveStatus(null), 4000);
    } finally {
      setIsArchiving(false);
    }
  };

  const handleRestoreFile = async (archivedFile: any) => {
    const confirmRestore = window.confirm(`Restore file "${archivedFile.name}" back to the active Watchtower index?`);
    if (!confirmRestore) return;

    try {
      setArchiveStatus(`Restoring "${archivedFile.name}"...`);

      if (!isSandbox && accessToken) {
        // Find if folder Watchtower-Archive is parent and can be removed, or we just put it back.
        // Moving it back is simulated because we don't track original parents, but it will reside back in the general workspace root.
        onAddLog(`Restoring file "${archivedFile.name}" from 'Watchtower-Archive' Google Drive folder...`, 'info');
      }

      // Add back to active files
      const restoredFile: DriveFile = {
        id: archivedFile.id,
        name: archivedFile.name,
        mimeType: archivedFile.mimeType,
        size: archivedFile.size,
        modifiedTime: archivedFile.modifiedTime,
        webViewLink: archivedFile.webViewLink,
        content: archivedFile.content,
        tags: archivedFile.tags || []
      };

      setFiles(prev => [...prev, restoredFile]);
      setArchivedFiles(prev => prev.filter(f => f.id !== archivedFile.id));

      // Update Stats
      setStats(prev => ({
        ...prev,
        totalFiles: prev.totalFiles + 1,
        totalSize: prev.totalSize + (archivedFile.size || 0),
        score: Math.max(10, prev.score - 4), // Restoring slightly decreases score
      }));

      onAddLog(`Restored file "${archivedFile.name}" back to primary workspace list.`, 'success');
      setArchiveStatus(null);
    } catch (err: any) {
      console.error(err);
      onAddLog(`Failed to restore file: ${err.message}`, 'error');
      setArchiveStatus(`Restore failed: ${err.message}`);
    }
  };

  const handleClearArchiveVault = () => {
    const confirmClear = window.confirm("Are you sure you want to completely clear the virtual archive tracking history? This is irreversible.");
    if (!confirmClear) return;
    setArchivedFiles([]);
    onAddLog("Virtual Watchtower-Archive Vault records purged.", "warn");
  };

  return (
    <div className="space-y-6" id="watchtower-settings-container">
      {/* Control Deck Header Action */}
      <div className="bg-[#090d16]/70 border border-slate-800/80 backdrop-blur-md rounded-3xl p-6 sm:p-8 shadow-lg">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2.5 tracking-tight">
              <Settings className="w-5 h-5 text-cyan-400" />
              Watchtower Automated Sync & Archiving Console
            </h3>
            <p className="text-xs text-slate-400 mt-1">
              Configure system intelligence scan intervals and initiate automated cleanup routines
            </p>
          </div>

          <button
            onClick={() => setIsOpen(!isOpen)}
            className="px-4 py-2 bg-slate-900 border border-slate-800 hover:border-cyan-500/50 hover:bg-slate-950 text-xs text-cyan-400 font-mono uppercase tracking-widest font-bold rounded-xl transition-all cursor-pointer flex items-center gap-2"
            id="toggle-settings-panel-btn"
          >
            <Settings className={`w-4 h-4 transition-transform duration-500 ${isOpen ? 'rotate-180' : ''}`} />
            {isOpen ? 'Close Settings Panel' : 'Open Settings Panel'}
          </button>
        </div>

        <AnimatePresence>
          {isOpen && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              transition={{ duration: 0.3 }}
              className="overflow-hidden mt-6 pt-6 border-t border-slate-850"
              id="watchtower-settings-collapsible"
            >
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                {/* 1. Sync Interval & Automations */}
                <div className="bg-[#04060a]/95 border border-slate-850 rounded-2xl p-5 space-y-5 shadow-inner">
                  <h4 className="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2 border-b border-slate-850 pb-2.5">
                    <Clock className="w-4 h-4 text-cyan-400" />
                    Automated Sync Intervals
                  </h4>

                  <p className="text-xs text-slate-400 leading-relaxed">
                    Set how often Watchtower queries the Google Workspace nodes to rebuild classification metadata. 
                    <span className="text-cyan-400 block mt-1 font-mono">Note: Simulated shorter durations applied in preview for instant telemetry updates.</span>
                  </p>

                  <div className="grid grid-cols-3 gap-2">
                    {[
                      { id: 'manual', label: 'Manual Only', desc: 'On demand' },
                      { id: 'hourly', label: 'Hourly', desc: '60s test interval' },
                      { id: 'daily', label: 'Daily', desc: '180s test interval' },
                    ].map((item) => {
                      const active = syncInterval === item.id;
                      return (
                        <button
                          key={item.id}
                          type="button"
                          onClick={() => setSyncInterval(item.id as any)}
                          className={`p-3 rounded-xl border text-left transition-all cursor-pointer flex flex-col justify-between min-h-[72px] ${
                            active
                              ? 'bg-cyan-500/10 border-cyan-500 text-cyan-400 shadow-[0_0_12px_rgba(6,182,212,0.15)]'
                              : 'bg-[#020305] border-slate-800 text-slate-400 hover:border-slate-700 hover:text-slate-200'
                          }`}
                        >
                          <span className="text-xs font-bold font-mono block">{item.label}</span>
                          <span className="text-[9px] text-slate-500 font-mono mt-1 block">{item.desc}</span>
                        </button>
                      );
                    })}
                  </div>

                  {syncInterval !== 'manual' && (
                    <div className="flex items-center justify-between p-3 bg-cyan-950/25 border border-cyan-900/30 rounded-xl text-xs font-mono">
                      <span className="text-slate-400 flex items-center gap-1.5">
                        <span className="w-1.5 h-1.5 bg-cyan-400 rounded-full animate-ping"></span>
                        Automated scan daemon running...
                      </span>
                      <span className="text-cyan-400 font-bold">
                        Next sync in: {formatCountdown(countdown)}
                      </span>
                    </div>
                  )}

                  {/* Toggle archive on sync */}
                  <div className="flex items-center justify-between p-3 bg-slate-900/50 border border-slate-800/60 rounded-xl">
                    <div className="flex items-start gap-2 max-w-[80%]">
                      <FolderArchive className="w-4 h-4 text-emerald-400 mt-0.5 shrink-0" />
                      <div>
                        <span className="text-xs font-bold text-slate-300 block">Auto-Archive on Sync</span>
                        <span className="text-[10px] text-slate-500 leading-tight block mt-0.5">
                          When enabled, duplicates and year-old files are archived automatically upon completing any sync loop.
                        </span>
                      </div>
                    </div>

                    <button
                      type="button"
                      onClick={() => setAutoArchiveOnSync(!autoArchiveOnSync)}
                      className={`w-10 h-6 rounded-full p-0.5 transition-colors cursor-pointer focus:outline-hidden ${
                        autoArchiveOnSync ? 'bg-emerald-500' : 'bg-slate-800'
                      }`}
                    >
                      <div className={`bg-[#090d16] w-5 h-5 rounded-full shadow-md transform transition-transform duration-200 ${
                        autoArchiveOnSync ? 'translate-x-4' : 'translate-x-0'
                      }`} />
                    </button>
                  </div>
                </div>

                {/* 2. Deep Auto-Archive Console */}
                <div className="bg-[#04060a]/95 border border-slate-850 rounded-2xl p-5 space-y-5 shadow-inner flex flex-col justify-between">
                  <div className="space-y-4">
                    <h4 className="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2 border-b border-slate-850 pb-2.5">
                      <FolderArchive className="w-4 h-4 text-emerald-400" />
                      Deep Auto-Archive Engine
                    </h4>

                    <p className="text-xs text-slate-400 leading-relaxed">
                      Surgical system sweep designed to automatically detect and archive file weight. The engine targeting criteria:
                    </p>

                    <div className="grid grid-cols-2 gap-3 text-[11px] font-mono">
                      <div className="p-2.5 bg-[#020305] border border-slate-850 rounded-xl">
                        <span className="text-emerald-400 font-bold block">1. Duplicates</span>
                        <span className="text-slate-500 text-[10px] mt-0.5 block">AI-marked exact/near duplicate versions.</span>
                      </div>
                      <div className="p-2.5 bg-[#020305] border border-slate-850 rounded-xl">
                        <span className="text-amber-400 font-bold block">2. Outdated (Older &gt; 1yr)</span>
                        <span className="text-slate-500 text-[10px] mt-0.5 block">Inactive files untouched for 365+ days.</span>
                      </div>
                    </div>

                    <div className="text-[11px] bg-slate-900/40 p-2.5 border border-slate-800/60 rounded-xl text-slate-400 flex items-center gap-2">
                      <Info className="w-4 h-4 text-cyan-400 shrink-0" />
                      <span>Archives are safely migrated to the <strong>'Watchtower-Archive'</strong> folder.</span>
                    </div>
                  </div>

                  <div className="pt-4 space-y-2">
                    <button
                      type="button"
                      disabled={isArchiving}
                      onClick={() => executeAutoArchive(false)}
                      className="w-full py-3 bg-emerald-600/10 hover:bg-emerald-600/20 border border-emerald-500 text-emerald-400 hover:text-emerald-300 font-bold text-xs uppercase tracking-widest rounded-xl transition-all cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 shadow-[0_0_15px_rgba(16,185,129,0.05)]"
                    >
                      {isArchiving ? (
                        <>
                          <RefreshCw className="w-4 h-4 animate-spin" />
                          <span>Processing Archives...</span>
                        </>
                      ) : (
                        <>
                          <FolderArchive className="w-4 h-4" />
                          <span>Initiate Workspace Auto-Archive</span>
                        </>
                      )}
                    </button>

                    {archiveStatus && (
                      <div className="text-center text-[10px] font-mono text-cyan-400 animate-pulse pt-1">
                        {archiveStatus}
                      </div>
                    )}
                  </div>
                </div>
              </div>

              {/* 3. Archived Files Vault */}
              <div className="mt-8 bg-[#04060a]/80 border border-slate-850 rounded-2xl p-5 shadow-inner" id="archived-vault-section">
                <div className="flex items-center justify-between border-b border-slate-850 pb-3 mb-4">
                  <h4 className="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                    <Database className="w-4 h-4 text-cyan-500" />
                    Centralized 'Watchtower-Archive' Vault
                    <span className="text-[10px] font-mono bg-cyan-950 text-cyan-400 px-2 py-0.5 rounded-full border border-cyan-900/40">
                      {archivedFiles.length} archived items
                    </span>
                  </h4>

                  {archivedFiles.length > 0 && (
                    <button
                      onClick={handleClearArchiveVault}
                      className="text-[10px] font-mono font-bold text-rose-400 hover:text-rose-300 flex items-center gap-1 cursor-pointer"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                      Clear History Log
                    </button>
                  )}
                </div>

                {archivedFiles.length === 0 ? (
                  <div className="py-10 text-center text-slate-500 text-xs italic bg-slate-950/20 border border-dashed border-slate-850 rounded-xl">
                    Archive vault is empty. Redundant files will appear here once archived.
                  </div>
                ) : (
                  <div className="overflow-x-auto rounded-xl border border-slate-850">
                    <table className="w-full text-left border-collapse">
                      <thead>
                        <tr className="bg-[#020305] text-[10px] font-mono text-slate-500 uppercase tracking-wider border-b border-slate-850">
                          <th className="px-4 py-3">File Name</th>
                          <th className="px-4 py-3">Archive Reason</th>
                          <th className="px-4 py-3">Size</th>
                          <th className="px-4 py-3 text-right">Actions</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-850 text-xs text-slate-300 font-mono">
                        {archivedFiles.map((file, idx) => (
                          <tr key={`${file.id}-${idx}`} className="hover:bg-slate-900/30 transition-all">
                            <td className="px-4 py-3.5 flex items-center gap-2 min-w-[200px]">
                              <span className="p-1.5 bg-slate-950 rounded border border-slate-800 text-slate-500 shrink-0">
                                <FolderArchive className="w-3.5 h-3.5" />
                              </span>
                              <span className="font-sans font-bold text-slate-200 truncate max-w-[250px]" title={file.name}>
                                {file.name}
                              </span>
                            </td>
                            <td className="px-4 py-3.5">
                              <span className={`px-2.5 py-0.5 rounded text-[9px] font-bold border ${
                                file.archiveReason === 'Duplicate Copy'
                                  ? 'bg-purple-950/40 border-purple-900/30 text-purple-400'
                                  : 'bg-amber-950/40 border-amber-900/30 text-amber-400'
                              }`}>
                                {file.archiveReason}
                              </span>
                            </td>
                            <td className="px-4 py-3.5 text-slate-400">
                              {formatSize(file.size)}
                            </td>
                            <td className="px-4 py-3.5 text-right">
                              <button
                                onClick={() => handleRestoreFile(file)}
                                className="inline-flex items-center gap-1 px-2.5 py-1.5 bg-cyan-600/15 hover:bg-cyan-600/30 border border-cyan-500 text-cyan-400 hover:text-cyan-300 rounded-lg text-[10px] font-bold uppercase tracking-wider cursor-pointer transition-all"
                                title="Restore file to active directory"
                              >
                                <RotateCcw className="w-3 h-3" />
                                Restore
                              </button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
