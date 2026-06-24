/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export interface DriveFile {
  id: string;
  name: string;
  mimeType: string;
  size?: number;
  modifiedTime: string;
  webViewLink?: string;
  content?: string;
  tags?: string[];
}

export interface WatchtowerStats {
  totalFiles: number;
  totalSize: number;
  mimeTypeBreakdown: { name: string; value: number }[];
  sizeBreakdown: { name: string; value: number }[];
  lastSyncTime: string;
  score: number;
}

export interface CleanUpRecommendation {
  id: string;
  fileName: string;
  reason: string;
  size?: number;
  type: 'old' | 'duplicate' | 'large' | 'near-duplicate' | 'orphaned';
  confidence?: number;
  impact?: 'High' | 'Medium' | 'Low';
  suggestedAction?: string;
}

export interface ActivityLog {
  id: string;
  fileName: string;
  action: string;
  timestamp: string;
  user: string;
}

export interface AnalysisResult {
  fileId: string;
  fileName: string;
  summary: string;
  keyTakeaways: string[];
  actionItems: string[];
  projectCategory: string;
  categoryScore: number;
}

export interface LogEntry {
  id: string;
  timestamp: string;
  message: string;
  type: 'info' | 'success' | 'warn' | 'error' | 'neural' | 'system';
}
