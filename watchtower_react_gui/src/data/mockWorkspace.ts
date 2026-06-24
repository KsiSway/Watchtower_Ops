---------------------------------------------------------------
/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { DriveFile, WatchtowerStats, CleanUpRecommendation, ActivityLog } from '../types';

export const mockFiles: DriveFile[] = [
  {
    id: 'doc-q3-marketing',
    name: 'Q3 Product Marketing Strategy.gdoc',
    mimeType: 'application/vnd.google-apps.document',
    size: 24500,
    modifiedTime: '2026-06-22T14:30:00Z',
    content: `
# Q3 Product Marketing Strategy & Goals

## Executive Summary
This document outlines our strategy for the Q3 launch of Workspace Watchtower. Our focus is on positioning the product as an elegant, essential intelligence layer for personal and team file management.

## Key Target Audiences
1. Power Google Workspace users with over 10GB of scattered files.
2. Independent creators and consultants who manage dozens of active client folders.
3. Operations managers looking to optimize digital workspace hygiene.

## Core Messaging Pillars
- **Personal Intelligence**: Smarter summaries, not just search.
- **Architectural Honesty**: Zero fluff, high performance, and beautiful visual clarity.
- **Actionable Cleanup**: Declutter your digital life in 3 clicks.

## Action Items
- [ ] draft and finalize press release copy by July 15 (John)
- [ ] Configure marketing analytics trackers and GA4 tags (Sarah)
- [ ] Schedule product showcase webinar for August 1 (Elena)
    `
  },
  {
    id: 'sheet-financials',
    name: 'Q2 Financial Forecast.gsheet',
    mimeType: 'application/vnd.google-apps.spreadsheet',
    size: 158000,
    modifiedTime: '2026-06-21T09:15:00Z',
    content: `
Sheet Name: Revenue Forecast
Row 1: Month, Projected Revenue, Actual Revenue, Variance %
Row 2: April, $45,000, $48,200, +7.1%
Row 3: May, $48,000, $51,000, +6.25%
Row 4: June, $52,000, $56,400, +8.46%
Row 5: July, $58,000, N/A, N/A

Sheet Name: Operating Expenses
Row 1: Category, Budgeted, Spent, Remaining
Row 2: Marketing, $12,000, $11,400, $600
Row 3: Hosting & Compute, $4,500, $4,850, -$350
Row 4: Contractor Fees, $22,000, $21,500, $500
Row 5: Miscellaneous, $2,000, $1,800, $200
    `
  },
  {
    id: 'doc-old-spec',
    name: 'Backup Draft - Watchtower Spec v1 (OLD).gdoc',
    mimeType: 'application/vnd.google-apps.document',
    size: 12000,
    modifiedTime: '2024-03-12T11:00:00Z',
    content: `
# DEPRECATED - Workspace Watchtower Specification v1 (Archived)
This specification is obsolete. Please refer to version 3.2 for the current implementation details.
Old core design involved a local sqlite database synced over webdav, which has been replaced with server-side Firebase & Google Cloud synchronization.
    `
  },
  {
    id: 'sheet-duplicate',
    name: 'Q2 Financial Forecast (Copy).gsheet',
    mimeType: 'application/vnd.google-apps.spreadsheet',
    size: 158000,
    modifiedTime: '2026-06-21T09:16:00Z',
    content: `
Sheet Name: Revenue Forecast
Row 1: Month, Projected Revenue, Actual Revenue, Variance %
Row 2: April, $45,000, $48,200, +7.1%
Row 3: May, $48,000, $51,000, +6.25%
Row 4: June, $52,000, $56,400, +8.46%
Row 5: July, $58,000, N/A, N/A
    `
  },
  {
    id: 'pdf-logo-assets',
    name: 'High-Res Hero Assets Bundle.zip',
    mimeType: 'application/zip',
    size: 85200000, // ~81MB
    modifiedTime: '2025-11-05T16:45:00Z',
    content: 'Binary file archive containing source design assets, Figma exports, and raw marketing images.'
  },
  {
    id: 'doc-meeting-minutes',
    name: 'Sprint Planning Meeting Minutes - June 20.gdoc',
    mimeType: 'application/vnd.google-apps.document',
    size: 8500,
    modifiedTime: '2026-06-20T17:00:00Z',
    content: `
# sprint Planning Meeting Minutes - June 20, 2026

## Attendees
- Alex (Product Owner)
- Maya (Tech Lead)
- Toby (Frontend Dev)
- Lucas (Backend Dev)

## Discussion Notes
We finalized the user flows for Google Drive & Sheets scanning. Maya emphasized the importance of displaying a gorgeous, responsive, custom-styled dashboard. Toby suggested adding a Watchtower score to make workspace cleanup more interactive.

## Action Items
- [ ] Design custom radial score meter and bento grids (Toby)
- [ ] Connect Express proxy routes for Gemini 3.5 Flash (Lucas)
- [ ] Write robust sandbox fallback for rapid workspace previewing (Maya)
    `
  },
  {
    id: 'sheet-client-directory',
    name: 'Active Client Directories & Leads.gsheet',
    mimeType: 'application/vnd.google-apps.spreadsheet',
    size: 45000,
    modifiedTime: '2026-06-18T10:30:00Z',
    content: `
Sheet Name: Active Clients
Row 1: Company, Primary Contact, Email, Status, Monthly Retainer
Row 2: Nexus Technologies, Roger Lin, roger@nexus.io, Active, $6,500
Row 3: Prism Creative, Clara Oswald, clara@prism.co, Onboarding, $4,800
Row 4: Vanguard Security, James Smith, james@vanguard.com, Active, $8,200

Sheet Name: Lead Pipeline
Row 1: Lead Name, Company, Estimated Value, Interest Level, Last Contacted
Row 2: Sarah Connor, Cyberdyne Systems, $15,000, High, 2026-06-15
Row 3: John Doe, ACME Corp, $5,000, Medium, 2026-06-12
    `
  },
  {
    id: 'pdf-security-policy',
    name: 'Corporate Security Guidelines & Compliance.pdf',
    mimeType: 'application/pdf',
    size: 4200000, // ~4MB
    modifiedTime: '2025-01-10T12:00:00Z',
    content: 'Comprehensive regulatory overview, password compliance criteria, and incident response playbook.'
  },
  {
    id: 'doc-meeting-minutes-copy',
    name: 'Sprint Planning Meeting Minutes - June 20 (1).gdoc',
    mimeType: 'application/vnd.google-apps.document',
    size: 8500,
    modifiedTime: '2026-06-20T17:05:00Z',
    content: `
# sprint Planning Meeting Minutes - June 20, 2026

## Attendees
- Alex (Product Owner)
- Maya (Tech Lead)
- Toby (Frontend Dev)
- Lucas (Backend Dev)

## Discussion Notes
We finalized the user flows for Google Drive & Sheets scanning.
    `
  },
  {
    id: 'pdf-security-policy-copy',
    name: 'Corporate Security Guidelines & Compliance - copy.pdf',
    mimeType: 'application/pdf',
    size: 4200000,
    modifiedTime: '2025-01-10T12:05:00Z',
    content: 'Comprehensive regulatory overview, password compliance criteria, and incident response playbook.'
  }
];

export const mockStats: WatchtowerStats = {
  totalFiles: mockFiles.length,
  totalSize: mockFiles.reduce((acc, f) => acc + (f.size || 0), 0),
  mimeTypeBreakdown: [
    { name: 'Google Docs', value: 3 },
    { name: 'Google Sheets', value: 3 },
    { name: 'Archives / ZIP', value: 1 },
    { name: 'PDF Documents', value: 1 }
  ],
  sizeBreakdown: [
    { name: 'High-Res Hero Assets Bundle.zip', value: 85200000 },
    { name: 'Corporate Security Guidelines & Compliance.pdf', value: 4200000 },
    { name: 'Q2 Financial Forecast.gsheet', value: 158000 },
    { name: 'Other Files', value: 77000 }
  ],
  lastSyncTime: new Date().toISOString(),
  score: 68
};

export const mockRecommendations: CleanUpRecommendation[] = [
  {
    id: 'doc-old-spec',
    fileName: 'Backup Draft - Watchtower Spec v1 (OLD).gdoc',
    reason: 'Stale file (last modified in March 2024, over 2 years ago) containing obsolete spec drafts.',
    size: 12000,
    type: 'old'
  },
  {
    id: 'sheet-duplicate',
    fileName: 'Q2 Financial Forecast (Copy).gsheet',
    reason: 'Possible duplicate. Matches name and size with Q2 Financial Forecast.gsheet (created 1 min apart).',
    size: 158000,
    type: 'duplicate'
  },
  {
    id: 'pdf-logo-assets',
    fileName: 'High-Res Hero Assets Bundle.zip',
    reason: 'Very large file (85.2 MB) taking up 95% of workspace storage. Has not been modified in over 7 months.',
    size: 85200000,
    type: 'large'
  }
];

export const mockActivity: ActivityLog[] = [
  {
    id: 'act-1',
    fileName: 'Q3 Product Marketing Strategy.gdoc',
    action: 'Modified file properties and content',
    timestamp: '2026-06-22T14:30:00Z',
    user: 'Cleeman'
  },
  {
    id: 'act-2',
    fileName: 'Q2 Financial Forecast.gsheet',
    action: 'Updated actual revenue numbers for June',
    timestamp: '2026-06-21T09:15:00Z',
    user: 'Cleeman'
  },
  {
    id: 'act-3',
    fileName: 'Sprint Planning Meeting Minutes - June 20.gdoc',
    action: 'Created document',
    timestamp: '2026-06-20T17:00:00Z',
    user: 'Maya'
  }
];
