/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { Search, Filter, SortAsc, FileSpreadsheet, FileText, File, ExternalLink, RefreshCw, Trash2, ChevronDown, ChevronUp, X, CheckCircle2, AlertTriangle } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { DriveFile } from '../types';

interface FileListProps {
  files: DriveFile[];
  onSelectFile: (file: DriveFile) => void;
  selectedFileId?: string;
  isSyncing: boolean;
  onRefresh: () => void;
  onBulkCleanUp?: (ids: string[]) => Promise<void>;
  onUpdateTags?: (fileId: string, tags: string[]) => void;
}

type FileCategory = 'all' | 'documents' | 'spreadsheets' | 'other';

const parseSizeInBytes = (sizeStr: string): number | null => {
  const match = sizeStr.trim().match(/^([0-9.]+)\s*(b|kb|mb|gb)?$/i);
  if (!match) return null;
  const num = parseFloat(match[1]);
  const unit = (match[2] || 'b').toLowerCase();
  if (unit === 'b') return num;
  if (unit === 'kb') return num * 1024;
  if (unit === 'mb') return num * 1024 * 1024;
  if (unit === 'gb') return num * 1024 * 1024 * 1024;
  return num;
};

const matchSizeOperator = (fileSize: number | undefined, val: string): boolean => {
  if (fileSize === undefined) return false;
  const match = val.trim().match(/^([><]=?|=)?\s*(.*)$/);
  if (!match) return false;
  const op = match[1] || '=';
  const sizeValueStr = match[2];
  const bytes = parseSizeInBytes(sizeValueStr);
  if (bytes === null) return false;

  switch (op) {
    case '>': return fileSize > bytes;
    case '<': return fileSize < bytes;
    case '>=': return fileSize >= bytes;
    case '<=': return fileSize <= bytes;
    case '=':
    default:
      return fileSize === bytes;
  }
};

const matchTypeOperator = (file: DriveFile, val: string): boolean => {
  const mime = file.mimeType.toLowerCase();
  const name = file.name.toLowerCase();
  const v = val.toLowerCase();
  if (v === 'pdf') {
    return name.endsWith('.pdf') || mime.includes('pdf');
  }
  if (v === 'doc' || v === 'docx' || v === 'document') {
    return name.endsWith('.doc') || name.endsWith('.docx') || mime.includes('document');
  }
  if (v === 'sheet' || v === 'xlsx' || v === 'xls' || v === 'spreadsheet') {
    return name.endsWith('.xls') || name.endsWith('.xlsx') || mime.includes('spreadsheet');
  }
  if (v === 'csv') {
    return name.endsWith('.csv') || mime.includes('csv');
  }
  if (v === 'text' || v === 'txt') {
    return name.endsWith('.txt') || mime.includes('text') || mime.includes('plain');
  }
  return mime.includes(v) || name.includes(v);
};

const matchModifiedOperator = (modifiedTimeStr: string, val: string): boolean => {
  const match = val.trim().match(/^([><]=?|=)?\s*([0-9.]+)\s*(d|day|days)?$/i);
  if (!match) return false;
  const op = match[1] || '<';
  const days = parseFloat(match[2]);
  if (isNaN(days)) return false;
  
  const diffMs = Date.now() - new Date(modifiedTimeStr).getTime();
  const diffDays = diffMs / (1000 * 60 * 60 * 24);
  
  switch (op) {
    case '>': return diffDays > days;
    case '<': return diffDays < days;
    case '>=': return diffDays >= days;
    case '<=': return diffDays <= days;
    case '=':
    default:
      return Math.floor(diffDays) === Math.floor(days);
  }
};

const parseSearchTerm = (search: string) => {
  const tokens: string[] = [];
  const regex = /[^\s"']+|"([^"]*)"|'([^']*)'/g;
  let match;
  while ((match = regex.exec(search)) !== null) {
    tokens.push(match[1] || match[2] || match[0]);
  }

  const operators: { key: string; val: string }[] = [];
  const textTerms: string[] = [];

  for (const token of tokens) {
    if (token.includes(':')) {
      const idx = token.indexOf(':');
      const key = token.substring(0, idx).toLowerCase().trim();
      const val = token.substring(idx + 1).trim();
      operators.push({ key, val });
    } else {
      textTerms.push(token);
    }
  }

  return { operators, textTerms };
};

export default function FileList({
  files,
  onSelectFile,
  selectedFileId,
  isSyncing,
  onRefresh,
  onBulkCleanUp,
  onUpdateTags,
}: FileListProps) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<FileCategory>('all');
  const [selectedTag, setSelectedTag] = useState<string>('all');
  const [sortBy, setSortBy] = useState<'name' | 'name-asc' | 'name-desc' | 'date' | 'date-desc' | 'date-asc' | 'size' | 'size-desc' | 'size-asc' | 'tags-desc' | 'tags-asc'>('date-desc');
  const [isSortDropdownOpen, setIsSortDropdownOpen] = useState(false);
  const [selectedIds, setSelectedIds] = useState<string[]>([]);
  const [expandedFileId, setExpandedFileId] = useState<string | null>(null);

  // Sync selectedIds with existing files to remove any deleted ones
  useEffect(() => {
    const fileIdSet = new Set(files.map(f => f.id));
    setSelectedIds(prev => prev.filter(id => fileIdSet.has(id)));
  }, [files]);

  const getFileIcon = (mimeType: string) => {
    if (mimeType.includes('document')) {
      return <FileText className="w-4 h-4 text-cyan-400" />;
    }
    if (mimeType.includes('spreadsheet')) {
      return <FileSpreadsheet className="w-4 h-4 text-emerald-400" />;
    }
    return <File className="w-4 h-4 text-amber-400" />;
  };

  const getFileBadge = (mimeType: string) => {
    if (mimeType.includes('document')) {
      return <span className="px-2 py-0.5 bg-cyan-950/50 border border-cyan-800/30 text-cyan-400 rounded-md text-[10px] font-bold font-mono">Doc</span>;
    }
    if (mimeType.includes('spreadsheet')) {
      return <span className="px-2 py-0.5 bg-emerald-950/50 border border-emerald-800/30 text-emerald-400 rounded-md text-[10px] font-bold font-mono">Sheet</span>;
    }
    return <span className="px-2 py-0.5 bg-amber-950/50 border border-amber-800/30 text-amber-400 rounded-md text-[10px] font-bold font-mono">Binary</span>;
  };

  const getFileStatusIndicator = (file: DriveFile, index: number) => {
    if (isSyncing && (index % 3 === 0)) {
      return (
        <span className="px-1.5 py-0.5 bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 rounded-md text-[9px] font-mono flex items-center gap-1 shrink-0 select-none animate-pulse">
          <RefreshCw className="w-2.5 h-2.5 animate-spin" />
          <span>Syncing</span>
        </span>
      );
    }

    const isLarge = file.size && file.size > 2 * 1024 * 1024;
    const nameLower = file.name.toLowerCase();
    const isDuplicateOrDeprecated = 
      nameLower.includes('copy') || 
      nameLower.includes('backup') || 
      nameLower.includes('old') || 
      nameLower.includes('(1)') || 
      (file.tags && file.tags.some(t => ['duplicate', 'stale', 'deprecated', 'redundant'].includes(t.toLowerCase())));

    if (isLarge || isDuplicateOrDeprecated) {
      return (
        <span className="px-1.5 py-0.5 bg-amber-500/10 border border-amber-500/25 text-amber-400 rounded-md text-[9px] font-mono flex items-center gap-1 shrink-0 select-none">
          <AlertTriangle className="w-2.5 h-2.5" />
          <span>Flagged</span>
        </span>
      );
    }

    return (
      <span className="px-1.5 py-0.5 bg-emerald-500/10 border border-emerald-500/25 text-emerald-400 rounded-md text-[9px] font-mono flex items-center gap-1 shrink-0 select-none">
        <CheckCircle2 className="w-2.5 h-2.5" />
        <span>Cleaned</span>
      </span>
    );
  };

  const formatSize = (bytes?: number) => {
    if (bytes === undefined) return 'N/A';
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  };

  const formatDate = (isoString: string) => {
    return new Date(isoString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
    });
  };

  // Filter & Sort core logic
  const filteredFiles = files
    .filter((file) => {
      // Category filter
      if (selectedCategory === 'documents') {
        const isDoc = file.mimeType.includes('document');
        if (!isDoc) return false;
      } else if (selectedCategory === 'spreadsheets') {
        const isSheet = file.mimeType.includes('spreadsheet');
        if (!isSheet) return false;
      } else if (selectedCategory === 'other') {
        const isOther = !file.mimeType.includes('document') && !file.mimeType.includes('spreadsheet');
        if (!isOther) return false;
      }

      // Tag filter
      if (selectedTag !== 'all') {
        if (!file.tags || !file.tags.includes(selectedTag)) {
          return false;
        }
      }

      // Advanced Search Operator logic (Name, MimeType, Content, Tags & Operators)
      if (searchTerm.trim()) {
        const { operators, textTerms } = parseSearchTerm(searchTerm);
        
        // All operators must match (AND)
        for (const op of operators) {
          if (op.key === 'type') {
            if (!matchTypeOperator(file, op.val)) return false;
          } else if (op.key === 'size') {
            if (!matchSizeOperator(file.size, op.val)) return false;
          } else if (op.key === 'tag' || op.key === 'tags') {
            const hasTag = file.tags && file.tags.some(t => t.toLowerCase().includes(op.val.toLowerCase()));
            if (!hasTag) return false;
          } else if (op.key === 'modified') {
            if (!matchModifiedOperator(file.modifiedTime, op.val)) return false;
          }
        }
        
        // All text terms must match (AND)
        for (const term of textTerms) {
          const lowerTerm = term.toLowerCase();
          const matches = 
            file.name.toLowerCase().includes(lowerTerm) ||
            file.mimeType.toLowerCase().includes(lowerTerm) ||
            (file.content && file.content.toLowerCase().includes(lowerTerm)) ||
            (file.tags && file.tags.some(t => t.toLowerCase().includes(lowerTerm)));
          if (!matches) return false;
        }
      }

      return true;
    })
    .sort((a, b) => {
      if (sortBy === 'name' || sortBy === 'name-asc') {
        return a.name.localeCompare(b.name);
      }
      if (sortBy === 'name-desc') {
        return b.name.localeCompare(a.name);
      }
      if (sortBy === 'size' || sortBy === 'size-desc') {
        return (b.size || 0) - (a.size || 0);
      }
      if (sortBy === 'size-asc') {
        return (a.size || 0) - (b.size || 0);
      }
      if (sortBy === 'date-asc') {
        return new Date(a.modifiedTime).getTime() - new Date(b.modifiedTime).getTime();
      }
      if (sortBy === 'tags-desc') {
        const aCount = a.tags ? a.tags.length : 0;
        const bCount = b.tags ? b.tags.length : 0;
        return bCount - aCount;
      }
      if (sortBy === 'tags-asc') {
        const aCount = a.tags ? a.tags.length : 0;
        const bCount = b.tags ? b.tags.length : 0;
        return aCount - bCount;
      }
      // default: date (modifiedTime) or date-desc
      return new Date(b.modifiedTime).getTime() - new Date(a.modifiedTime).getTime();
    });

  const allFilteredIds = filteredFiles.map(f => f.id);
  const isAllSelected = filteredFiles.length > 0 && allFilteredIds.every(id => selectedIds.includes(id));
  const uniqueTags = Array.from(new Set(files.flatMap(file => file.tags || []))).sort();

  const handleToggleSelectAll = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (isAllSelected) {
      setSelectedIds(prev => prev.filter(id => !allFilteredIds.includes(id)));
    } else {
      setSelectedIds(prev => {
        const next = [...prev];
        allFilteredIds.forEach(id => {
          if (!next.includes(id)) {
            next.push(id);
          }
        });
        return next;
      });
    }
  };

  const handleToggleSelect = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setSelectedIds(prev =>
      prev.includes(id) ? prev.filter(item => item !== id) : [...prev, id]
    );
  };

  const handleBulkDeleteTrigger = async () => {
    if (onBulkCleanUp) {
      await onBulkCleanUp(selectedIds);
      setSelectedIds([]);
    }
  };

  return (
    <div className="bg-[#090d16]/70 border border-slate-800/80 backdrop-blur-md rounded-3xl p-6 sm:p-8 shadow-lg" id="file-catalog-panel">
      {/* Title & Actions Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
        <div>
          <h3 className="text-lg font-bold text-slate-100 tracking-tight">Active File Catalog</h3>
          <p className="text-xs text-slate-400 mt-1">Listed below are synced Google Workspace document metadata logs</p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={onRefresh}
            disabled={isSyncing}
            className="flex items-center gap-2 px-4 py-2.5 bg-[#05070a] hover:bg-[#090d16] text-slate-300 hover:text-slate-100 rounded-xl transition-all border border-slate-800 text-xs font-mono tracking-wide cursor-pointer disabled:opacity-50"
            id="refresh-sync-btn"
            title="Force Scan & Sync"
          >
            <RefreshCw className={`w-4 h-4 text-cyan-400 ${isSyncing ? 'animate-spin' : ''}`} />
            <span>{isSyncing ? 'Syncing...' : 'Scan & Sync'}</span>
          </button>
        </div>
      </div>

      {/* Global Interactive Search Console */}
      <div className="bg-[#04060a]/90 border border-slate-850 rounded-2xl p-4 sm:p-5 mb-6 space-y-4 shadow-inner" id="global-search-console">
        <div className="relative flex-1 file-list-search-bar" id="search-input-wrapper">
          <Search className="w-4 h-4 text-slate-500 absolute left-4 top-1/2 -translate-y-1/2 transition-colors duration-250 group-focus-within:text-cyan-400" />
          <input
            type="text"
            placeholder="Search by file name, classification, or custom tags (e.g. type:pdf, tag:important, modified:<30d)..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-11 pr-24 py-3 bg-[#020305] border border-slate-800 rounded-xl text-xs focus:ring-1 focus:ring-cyan-500 focus:border-cyan-500/80 focus:outline-hidden text-slate-200 placeholder-slate-600 transition-all shadow-[inset_0_2px_4px_rgba(0,0,0,0.6)]"
            id="file-search-field"
            title="Search by name, tag, or content snippet. Supports operators like 'type:pdf', 'size:>2mb', 'tag:important', and 'modified:<30d'"
          />
          
          {/* Real-time Match Indicator & Clear Button */}
          <div className="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-2">
            <span className="text-[10px] bg-cyan-950/40 text-cyan-400 border border-cyan-800/40 px-2 py-0.5 rounded-md font-mono font-bold">
              {filteredFiles.length} {filteredFiles.length === 1 ? 'match' : 'matches'}
            </span>
            {searchTerm && (
              <button
                onClick={() => setSearchTerm('')}
                className="text-slate-500 hover:text-slate-300 transition-colors cursor-pointer p-1 rounded-md hover:bg-slate-800/60"
                id="clear-search-btn"
                title="Clear search query"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        </div>

        {/* Real-time Custom Tag Suggestion Bar */}
        <div className="flex flex-col gap-2 pt-1">
          <div className="flex flex-wrap items-center gap-2 text-[11px]">
            <span className="text-slate-500 font-mono uppercase tracking-wider font-semibold">Filter by Custom Tag:</span>
            
            <button
              onClick={() => setSelectedTag('all')}
              className={`px-2.5 py-1 rounded-md text-[10px] font-mono font-bold transition-all border ${
                selectedTag === 'all'
                  ? 'bg-cyan-500/10 border-cyan-500 text-cyan-400 shadow-[0_0_8px_rgba(6,182,212,0.15)]'
                  : 'bg-transparent border-slate-800/60 text-slate-400 hover:text-slate-300 hover:border-slate-700'
              }`}
            >
              All ({files.length})
            </button>

            {uniqueTags.map((tag) => {
              const fileCount = files.filter(f => f.tags && f.tags.includes(tag)).length;
              const isSelected = selectedTag === tag;
              return (
                <button
                  key={tag}
                  onClick={() => setSelectedTag(isSelected ? 'all' : tag)}
                  className={`px-2.5 py-1 rounded-md text-[10px] font-mono font-bold transition-all border flex items-center gap-1.5 ${
                    isSelected
                      ? 'bg-cyan-500/15 border-cyan-500 text-cyan-300 shadow-[0_0_10px_rgba(6,182,212,0.2)]'
                      : 'bg-transparent border-slate-800/60 text-slate-400 hover:text-cyan-400 hover:border-slate-850'
                  }`}
                  title={`Filter files tagged with "${tag}"`}
                >
                  <span>#{tag}</span>
                  <span className={`text-[9px] rounded px-1 ${
                    isSelected ? 'bg-cyan-950/60 text-cyan-400' : 'bg-slate-900/60 text-slate-500'
                  }`}>
                    {fileCount}
                  </span>
                </button>
              );
            })}

            {/* Clear Filters Button (Visible only when filtering is active) */}
            {(searchTerm || selectedTag !== 'all' || selectedCategory !== 'all') && (
              <button
                onClick={() => {
                  setSearchTerm('');
                  setSelectedTag('all');
                  setSelectedCategory('all');
                }}
                className="ml-auto flex items-center gap-1 px-2 py-1 text-[10px] font-mono text-rose-400 hover:text-rose-300 transition-colors border border-dashed border-rose-500/30 rounded hover:border-rose-500/50"
              >
                <X className="w-3 h-3" />
                Reset Filters
              </button>
            )}
          </div>
          
          <div className="text-[10px] text-slate-500 font-mono leading-relaxed pt-1 flex flex-wrap gap-x-4 gap-y-1">
            <span className="text-cyan-500/80 font-bold uppercase">PRO SEARCH:</span>
            <span>type:pdf|sheet|doc</span>
            <span>size:&gt;5mb|&lt;1mb</span>
            <span>tag:important</span>
            <span>modified:&lt;30d</span>
          </div>

          <div className="text-[10px] text-slate-500 font-mono leading-relaxed pt-2 flex flex-wrap items-center gap-x-3 gap-y-1.5 border-t border-slate-900/60 mt-2">
            <span className="text-cyan-500/80 font-bold uppercase">CORE SHORTCUTS:</span>
            <span className="flex items-center gap-1">
              <kbd className="px-1.5 py-0.5 bg-slate-950/80 border border-slate-800 text-cyan-400 font-bold rounded">Ctrl+S</kbd>
              <span>Sync</span>
            </span>
            <span className="flex items-center gap-1">
              <kbd className="px-1.5 py-0.5 bg-slate-950/80 border border-slate-800 text-cyan-400 font-bold rounded">Ctrl+F</kbd>
              <span>Find</span>
            </span>
            <span className="flex items-center gap-1">
              <kbd className="px-1.5 py-0.5 bg-slate-950/80 border border-slate-800 text-cyan-400 font-bold rounded">Ctrl+D</kbd>
              <span>Theme</span>
            </span>
            <span className="flex items-center gap-1">
              <kbd className="px-1.5 py-0.5 bg-slate-950/80 border border-slate-800 text-cyan-400 font-bold rounded">Ctrl+K</kbd>
              <span>Keys</span>
            </span>
          </div>
        </div>
      </div>

      {/* Tabs / Filter Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-850 pb-4 mb-6">
        <div className="flex items-center gap-1.5" id="category-filter-tabs">
          {(['all', 'documents', 'spreadsheets', 'other'] as FileCategory[]).map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all uppercase tracking-wider ${
                selectedCategory === cat
                  ? 'bg-cyan-600/20 border border-cyan-500 text-cyan-400'
                  : 'text-slate-500 hover:text-slate-300'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        <div className="flex flex-wrap items-center gap-4">
          {/* Sort Dropdown */}
          <div className="flex items-center gap-2 relative">
            <span className="text-xs text-slate-400 flex items-center gap-1 font-semibold">
              <SortAsc className="w-3.5 h-3.5" /> Sort:
            </span>
            <div className="relative">
              <button
                type="button"
                onClick={() => setIsSortDropdownOpen(!isSortDropdownOpen)}
                className="px-3 py-1.5 bg-[#05070a] border border-slate-800 text-xs text-slate-300 font-bold rounded-lg focus:outline-hidden font-mono flex items-center gap-2 hover:border-cyan-500/50 hover:text-cyan-400 transition-all cursor-pointer min-w-[210px] justify-between"
                id="file-sort-dropdown"
              >
                <span className="truncate">
                  {sortBy === 'date-desc' && 'Last Modified (Newest First)'}
                  {sortBy === 'date-asc' && 'Last Modified (Oldest First)'}
                  {sortBy === 'name-asc' && 'Filename (A-Z)'}
                  {sortBy === 'name-desc' && 'Filename (Z-A)'}
                  {sortBy === 'size-desc' && 'Size (Large to Small)'}
                  {sortBy === 'size-asc' && 'Size (Small to Large)'}
                  {sortBy === 'tags-desc' && 'Tag Count (Most First)'}
                  {sortBy === 'tags-asc' && 'Tag Count (Fewest First)'}
                </span>
                <ChevronDown className={`w-3.5 h-3.5 text-slate-500 shrink-0 transition-transform duration-200 ${isSortDropdownOpen ? 'rotate-180' : ''}`} />
              </button>

              <AnimatePresence>
                {isSortDropdownOpen && (
                  <>
                    <div 
                      className="fixed inset-0 z-20" 
                      onClick={() => setIsSortDropdownOpen(false)} 
                    />
                    <motion.div
                      initial={{ opacity: 0, y: -10, scale: 0.95 }}
                      animate={{ opacity: 1, y: 0, scale: 1 }}
                      exit={{ opacity: 0, y: -10, scale: 0.95 }}
                      transition={{ duration: 0.15 }}
                      className="absolute right-0 mt-1.5 w-60 bg-[#090d16] border border-slate-800 rounded-xl shadow-2xl shadow-black p-1.5 z-30 space-y-0.5 overflow-hidden"
                      id="file-sort-dropdown-menu"
                    >
                      {[
                        { value: 'date-desc', label: 'Last Modified (Newest First)' },
                        { value: 'date-asc', label: 'Last Modified (Oldest First)' },
                        { value: 'name-asc', label: 'Filename (A-Z)' },
                        { value: 'name-desc', label: 'Filename (Z-A)' },
                        { value: 'size-desc', label: 'Size (Large to Small)' },
                        { value: 'size-asc', label: 'Size (Small to Large)' },
                        { value: 'tags-desc', label: 'Tag Count (Most First)' },
                        { value: 'tags-asc', label: 'Tag Count (Fewest First)' },
                      ].map((opt) => {
                        const isSelected = sortBy === opt.value;
                        return (
                          <button
                            key={opt.value}
                            type="button"
                            onClick={() => {
                              setSortBy(opt.value as any);
                              setIsSortDropdownOpen(false);
                            }}
                            className={`w-full text-left px-3 py-2 rounded-lg text-xs font-mono font-medium transition-all flex items-center justify-between cursor-pointer ${
                              isSelected
                                ? 'bg-cyan-500/10 text-cyan-400 font-bold border border-cyan-500/20'
                                : 'text-slate-400 hover:bg-slate-900/60 hover:text-slate-200'
                            }`}
                          >
                            <span>{opt.label}</span>
                            {isSelected && <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />}
                          </button>
                        );
                      })}
                    </motion.div>
                  </>
                )}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </div>

      {/* Grid List */}
      <div className="overflow-x-auto">
        <table className="w-full text-left border-collapse" id="file-list-table">
          <thead>
            <tr className="border-b border-slate-850 text-xs font-bold text-slate-500 uppercase tracking-widest font-mono">
              <th className="py-3 px-4 w-12 text-center" onClick={(e) => e.stopPropagation()}>
                <div 
                  onClick={handleToggleSelectAll}
                  className={`w-5 h-5 rounded border flex items-center justify-center cursor-pointer transition-all mx-auto ${
                    isAllSelected 
                      ? 'bg-cyan-500/20 border-cyan-400 text-cyan-400 shadow-[0_0_8px_rgba(6,182,212,0.4)]' 
                      : 'border-slate-800 hover:border-cyan-500/60 bg-[#05070a]'
                  }`}
                  title={isAllSelected ? "Deselect All" : "Select All"}
                >
                  {isAllSelected && <div className="w-2 h-2 rounded-xs bg-cyan-400 animate-pulse" />}
                </div>
              </th>
              <th className="py-3 px-2 w-10 text-center" />
              <th className="py-3 px-4">Filename</th>
              <th className="py-3 px-4">Format</th>
              <th className="py-3 px-4">Tags</th>
              <th className="py-3 px-4">Size</th>
              <th className="py-3 px-4">Last Modified</th>
              <th className="py-3 px-4 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-850/80 text-xs text-slate-300">
            {filteredFiles.length > 0 ? (
              filteredFiles.map((file, idx) => {
                const isSelected = selectedFileId === file.id;
                const isRowChecked = selectedIds.includes(file.id);
                const isExpanded = expandedFileId === file.id;
                return (
                  <React.Fragment key={`${file.id}-${idx}`}>
                    <tr
                      className={`transition-all duration-300 group cursor-pointer border-b border-slate-900/40 transform hover:-translate-y-[1px] ${
                        isSelected 
                          ? 'bg-cyan-950/20 font-semibold shadow-[inset_0_0_15px_rgba(6,182,212,0.12)]' 
                          : isRowChecked
                            ? 'bg-cyan-950/10 font-medium'
                            : 'hover:bg-cyan-950/12 hover:shadow-[0_4px_16px_-4px_rgba(6,182,212,0.15)]'
                      } ${isExpanded ? 'bg-slate-900/40' : ''}`}
                      onClick={() => onSelectFile(file)}
                    >
                      <td className="py-4 px-4 text-center w-12" onClick={(e) => e.stopPropagation()}>
                        <div 
                          onClick={(e) => handleToggleSelect(file.id, e)}
                          className={`w-5 h-5 rounded border flex items-center justify-center cursor-pointer transition-all mx-auto ${
                            isRowChecked
                              ? 'bg-cyan-500/20 border-cyan-400 text-cyan-400 shadow-[0_0_8px_rgba(6,182,212,0.4)]' 
                              : 'border-slate-800 hover:border-cyan-500/60 bg-[#05070a] group-hover:border-cyan-500/40 group-hover:scale-105'
                          }`}
                          title={isRowChecked ? "Deselect" : "Select"}
                        >
                          {isRowChecked && (
                            <div className="w-2 h-2 rounded-xs bg-cyan-400" />
                          )}
                        </div>
                      </td>
                      <td className="py-4 px-2 text-center w-10" onClick={(e) => e.stopPropagation()}>
                        <button
                          onClick={() => setExpandedFileId(isExpanded ? null : file.id)}
                          className="p-1 hover:bg-slate-800 rounded transition-all duration-300 text-slate-400 hover:text-cyan-400 cursor-pointer flex items-center justify-center mx-auto group-hover:scale-110 group-hover:text-slate-300"
                          title={isExpanded ? "Collapse quick view" : "Expand quick view"}
                          id={`expand-btn-${file.id}`}
                        >
                          {isExpanded ? (
                            <ChevronUp className="w-4 h-4 text-cyan-400" />
                          ) : (
                            <ChevronDown className="w-4 h-4" />
                          )}
                        </button>
                      </td>
                      <td className={`py-4 px-4 flex items-center gap-2.5 max-w-xs sm:max-w-md truncate border-l-2 transition-all duration-300 ${
                        isSelected ? 'border-cyan-500' : 'border-transparent group-hover:border-cyan-400/60'
                      }`}>
                        <div className="transition-all duration-300 group-hover:translate-x-2 flex items-center justify-between gap-2.5 w-full truncate">
                          <div className="flex items-center gap-2.5 truncate">
                            <div className="transition-transform duration-300 group-hover:scale-115 shrink-0">
                              {getFileIcon(file.mimeType)}
                            </div>
                            <span className="truncate group-hover:text-cyan-400 transition-colors duration-300">{file.name}</span>
                          </div>
                          <div className="flex items-center gap-1.5 ml-2 shrink-0">
                            {getFileStatusIndicator(file, idx)}
                          </div>
                        </div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="transition-all duration-300 group-hover:translate-x-0.5 group-hover:scale-102 inline-block">
                          {getFileBadge(file.mimeType)}
                        </div>
                      </td>
                      <td className="py-4 px-4" onClick={(e) => e.stopPropagation()}>
                        <div className="flex flex-wrap gap-1.5 items-center">
                          {(file.tags || []).map(tag => (
                            <span 
                              key={tag} 
                              onClick={(e) => {
                                  e.stopPropagation();
                                  setSelectedTag(tag);
                              }}
                              className="px-2 py-0.5 bg-cyan-950/40 border border-cyan-800/40 text-cyan-300 rounded text-[9px] font-mono hover:bg-cyan-900/60 transition-all cursor-pointer inline-flex items-center gap-1 hover:scale-105 active:scale-95"
                              title="Click to filter by this tag"
                            >
                              {tag}
                              <button
                                type="button"
                                onClick={(e) => {
                                  e.stopPropagation();
                                  const updated = (file.tags || []).filter(t => t !== tag);
                                  onUpdateTags?.(file.id, updated);
                                }}
                                className="text-[9px] text-slate-500 hover:text-rose-400 font-bold ml-0.5 shrink-0"
                                title={`Remove tag: ${tag}`}
                              >
                                &times;
                              </button>
                            </span>
                          ))}
                          <form 
                            onSubmit={(e) => {
                              e.preventDefault();
                              const form = e.currentTarget;
                              const input = form.elements.namedItem('inlineTag') as HTMLInputElement;
                              const val = input.value.trim().toLowerCase();
                              if (val) {
                                const current = file.tags || [];
                                if (!current.includes(val)) {
                                  onUpdateTags?.(file.id, [...current, val]);
                                }
                                input.value = '';
                              }
                            }}
                            className="inline-flex items-center"
                          >
                            <input 
                              name="inlineTag"
                              type="text" 
                              placeholder="+ tag"
                              className="w-12 px-1.5 py-0.5 bg-[#030508] border border-slate-800 rounded text-[9px] text-slate-300 placeholder-slate-650 focus:outline-hidden focus:border-cyan-500 font-mono transition-all hover:w-16 focus:w-20"
                            />
                          </form>
                        </div>
                      </td>
                      <td className="py-4 px-4 font-mono text-slate-400">
                        <div className="transition-all duration-300 group-hover:translate-x-0.5 group-hover:text-slate-200">
                          {formatSize(file.size)}
                        </div>
                      </td>
                      <td className="py-4 px-4 text-slate-400 font-mono">
                        <div className="transition-all duration-300 group-hover:translate-x-0.5 group-hover:text-slate-200">
                          {formatDate(file.modifiedTime)}
                        </div>
                      </td>
                      <td className="py-4 px-4 text-right" onClick={(e) => e.stopPropagation()}>
                        <button
                          onClick={() => onSelectFile(file)}
                          className={`px-3 py-1.5 rounded-lg text-[10px] uppercase tracking-wider font-bold transition-all duration-300 hover:scale-105 ${
                            isSelected
                              ? 'bg-cyan-600/20 border border-cyan-500 text-cyan-400 cyber-glow-cyan'
                              : 'bg-slate-900 border border-slate-800 text-slate-300 hover:bg-slate-800 hover:border-slate-700 hover:text-slate-100 hover:shadow-[0_0_10px_rgba(6,182,212,0.15)] group-hover:border-cyan-500/40 group-hover:text-cyan-300'
                          }`}
                        >
                          Inspect
                        </button>
                      </td>
                    </tr>
                    {isExpanded && (
                      <tr className="bg-[#05070a]/40" id={`expanded-row-${file.id}`}>
                        <td colSpan={8} className="p-4 sm:p-6 border-b border-slate-850">
                          <motion.div
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: 'auto' }}
                            exit={{ opacity: 0, height: 0 }}
                            transition={{ duration: 0.25, ease: 'easeInOut' }}
                            className="overflow-hidden"
                          >
                            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 bg-[#040609] border border-cyan-950/40 rounded-2xl p-5 text-left" id={`expanded-content-${file.id}`}>
                              {/* Left Panel: Properties and stats */}
                              <div className="space-y-3.5 text-xs text-slate-300">
                                <h4 className="font-mono text-cyan-400 text-[10px] uppercase tracking-wider font-bold border-b border-slate-850 pb-2 flex items-center gap-2">
                                  <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />
                                  Heuristic Properties & Metadata
                                </h4>
                                <div className="space-y-2">
                                  <div className="grid grid-cols-3 gap-2 py-1 border-b border-slate-900/55">
                                    <span className="text-slate-500 font-mono text-[10px]">FILE IDENTIFIER:</span>
                                    <span className="col-span-2 font-mono text-slate-400 select-all truncate">{file.id}</span>
                                  </div>
                                  <div className="grid grid-cols-3 gap-2 py-1 border-b border-slate-900/55">
                                    <span className="text-slate-500 font-mono text-[10px]">MIME CLASSIFICATION:</span>
                                    <span className="col-span-2 font-mono text-slate-400 select-all truncate">{file.mimeType}</span>
                                  </div>
                                  <div className="grid grid-cols-3 gap-2 py-1 border-b border-slate-900/55">
                                    <span className="text-slate-500 font-mono text-[10px]">STORAGE FOOTPRINT:</span>
                                    <span className="col-span-2 font-mono text-slate-400">{(file.size ?? 0).toLocaleString()} Bytes ({formatSize(file.size)})</span>
                                  </div>
                                  <div className="grid grid-cols-3 gap-2 py-1 border-b border-slate-900/55">
                                    <span className="text-slate-500 font-mono text-[10px]">INDEX MODIFIED TIME:</span>
                                    <span className="col-span-2 font-mono text-slate-400">{formatDate(file.modifiedTime)} ({new Date(file.modifiedTime).toLocaleTimeString()})</span>
                                  </div>
                                </div>
                                {file.webViewLink && (
                                  <div className="pt-2">
                                    <a
                                      href={file.webViewLink}
                                      target="_blank"
                                      rel="noreferrer"
                                      className="inline-flex items-center gap-1.5 text-cyan-400 hover:text-cyan-300 hover:underline transition-colors font-mono font-bold text-[9px] uppercase tracking-wider"
                                    >
                                      <ExternalLink className="w-3 h-3" />
                                      Launch Google Drive Node
                                    </a>
                                  </div>
                                )}
                              </div>

                              {/* Right Panel: Code snippet content */}
                              <div className="space-y-2.5">
                                <div className="flex items-center justify-between border-b border-slate-850 pb-2">
                                  <h4 className="font-mono text-cyan-400 text-[10px] uppercase tracking-wider font-bold">
                                    Quick Content Preview
                                  </h4>
                                  <span className="text-[9px] text-slate-500 font-mono">Index Snippet</span>
                                </div>

                                {file.content ? (
                                  <div className="relative">
                                    <pre className="font-mono bg-[#010204]/90 p-4 rounded-xl border border-slate-900 max-h-40 overflow-y-auto text-slate-400 text-[10px] whitespace-pre-wrap leading-relaxed">
                                      {file.content}
                                    </pre>
                                  </div>
                                ) : (
                                  <div className="bg-[#010204]/90 border border-slate-900 rounded-xl p-6 text-center text-slate-500 italic text-[10px] font-mono">
                                    No immediate document content snippet cached for indexing. Double-click or click "Inspect" above to query neural embeddings.
                                  </div>
                                )}
                              </div>
                            </div>
                          </motion.div>
                        </td>
                      </tr>
                    )}
                  </React.Fragment>
                );
              })
            ) : (
              <tr>
                <td colSpan={8} className="py-12 text-center text-slate-500 italic">
                  No workspace files match the selected criteria.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Floating Bulk Delete Action Bar */}
      <AnimatePresence>
        {selectedIds.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: 50, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 50, scale: 0.95 }}
            className="fixed bottom-6 left-1/2 -translate-x-1/2 z-45 bg-[#090d16]/95 border border-cyan-500/40 backdrop-blur-md rounded-2xl px-6 py-4 shadow-[0_10px_50px_rgba(6,182,212,0.25)] flex flex-col sm:flex-row items-center gap-4 sm:gap-6 min-w-[320px] sm:min-w-[460px] justify-between text-xs tracking-wide"
            id="bulk-delete-bar"
          >
            <div className="flex items-center gap-3">
              <span className="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-ping" />
              <span className="font-mono text-slate-300">
                <strong className="text-cyan-400 font-extrabold text-sm">{selectedIds.length}</strong> {selectedIds.length === 1 ? 'file' : 'files'} selected for cleanup
              </span>
            </div>
            
            <div className="flex items-center gap-2">
              <button
                onClick={() => setSelectedIds([])}
                className="px-3 py-1.5 bg-slate-900 hover:bg-slate-850 border border-slate-800 text-slate-300 rounded-lg font-bold transition-all uppercase text-[10px] tracking-widest cursor-pointer"
              >
                Deselect
              </button>
              <button
                onClick={handleBulkDeleteTrigger}
                disabled={isSyncing}
                className="flex items-center gap-1.5 px-4 py-1.5 bg-rose-600/20 hover:bg-rose-600/35 border border-rose-500 text-rose-400 rounded-lg font-bold transition-all uppercase text-[10px] tracking-widest cursor-pointer disabled:opacity-55 disabled:pointer-events-none hover:shadow-[0_0_15px_rgba(239,68,68,0.25)]"
                id="bulk-delete-confirm-btn"
              >
                <Trash2 className="w-3.5 h-3.5" />
                Purge Selected
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
