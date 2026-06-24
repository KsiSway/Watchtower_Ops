/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { Database, ShieldCheck, Eye, Sparkles, Key, HelpCircle, Check, Play } from 'lucide-react';

interface GoogleConnectionProps {
  isSandbox: boolean;
  setIsSandbox: (val: boolean) => void;
  clientId: string;
  onConnect: (accessToken: string) => void;
  isConnected: boolean;
  onDisconnect: () => void;
  userEmail: string | null;
}

export default function GoogleConnection({
  isSandbox,
  setIsSandbox,
  clientId,
  onConnect,
  isConnected,
  onDisconnect,
  userEmail,
}: GoogleConnectionProps) {
  const [showGuide, setShowGuide] = useState(false);
  const [tokenInput, setTokenInput] = useState('');
  const [showDirectInput, setShowDirectInput] = useState(false);

  const handleLiveConnect = () => {
    if (!clientId) {
      setShowGuide(true);
      return;
    }

    // Initialize GIS client-side flow if available
    try {
      const gapi = (window as any).gapi;
      const google = (window as any).google;

      if (google?.accounts?.oauth2) {
        const client = google.accounts.oauth2.initTokenClient({
          client_id: clientId,
          scope: 'https://www.googleapis.com/auth/drive.readonly https://www.googleapis.com/auth/spreadsheets.readonly https://www.googleapis.com/auth/documents.readonly https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/gmail.send',
          callback: (response: any) => {
            if (response.access_token) {
              onConnect(response.access_token);
            }
          },
        });
        client.requestAccessToken();
      } else {
        // Fallback: Open popup redirect or let user input a developer access token
        setShowDirectInput(true);
      }
    } catch (err) {
      console.error('Error loading Google Identity Services:', err);
      setShowDirectInput(true);
    }
  };

  const handleManualTokenSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (tokenInput.trim()) {
      onConnect(tokenInput.trim());
      setShowDirectInput(false);
    }
  };

  return (
    <div className="bg-[#090d16]/70 border border-slate-800/80 backdrop-blur-md rounded-3xl p-6 sm:p-8 shadow-lg mb-8" id="google-connection-panel">
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div>
          <div className="flex items-center gap-3">
            <span className="p-2.5 bg-cyan-950/50 border border-cyan-500/30 text-cyan-400 rounded-xl">
              <Database className="w-5 h-5" />
            </span>
            <h2 className="text-xl font-bold text-slate-100 tracking-tight">Intelligence Integration Mode</h2>
          </div>
          <p className="text-sm text-slate-400 mt-2 max-w-xl leading-relaxed">
            Choose between <strong className="text-cyan-400">Sandbox Mode</strong> (using realistic file assets with live Gemini analysis) or connect your live <strong className="text-cyan-400">Google Drive & Workspace</strong> using your OAuth credentials.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3 w-full md:w-auto">
          <button
            onClick={() => {
              setIsSandbox(true);
              onDisconnect();
            }}
            className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 py-3 rounded-2xl text-xs uppercase tracking-widest font-bold transition-all duration-300 ${
              isSandbox
                ? 'bg-cyan-600/20 border border-cyan-500 text-cyan-400 cyber-glow-cyan'
                : 'bg-[#05070a] text-slate-500 hover:text-slate-300 border border-slate-800/80 hover:bg-[#090d16]'
            }`}
            id="sandbox-mode-btn"
          >
            <Eye className="w-4 h-4" />
            Sandbox Mode
          </button>

          <button
            onClick={() => {
              setIsSandbox(false);
              if (!isConnected) {
                handleLiveConnect();
              }
            }}
            className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 py-3 rounded-2xl text-xs uppercase tracking-widest font-bold transition-all duration-300 ${
              !isSandbox
                ? 'bg-emerald-600/20 border border-emerald-500 text-emerald-400'
                : 'bg-[#05070a] text-slate-500 hover:text-slate-300 border border-slate-800/80 hover:bg-[#090d16]'
            }`}
            id="live-mode-btn"
          >
            <Sparkles className="w-4 h-4" />
            Live Sync Mode
          </button>
        </div>
      </div>

      {/* Connected State */}
      {!isSandbox && isConnected && (
        <div className="mt-6 flex flex-col sm:flex-row items-center justify-between bg-emerald-950/20 border border-emerald-900/40 rounded-2xl p-4 gap-4" id="connection-status-success">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded-full">
              <Check className="w-4 h-4" />
            </div>
            <div>
              <p className="text-sm font-bold text-emerald-300">Successfully Connected</p>
              <p className="text-xs text-emerald-400/80 mt-0.5">
                Authorized to read Google Drive, Docs, and Sheets. Account: <span className="font-mono text-cyan-400">{userEmail || 'cleeman1989@gmail.com'}</span>
              </p>
            </div>
          </div>
          <button
            onClick={onDisconnect}
            className="text-xs font-bold text-emerald-400 hover:text-emerald-300 underline px-3 py-1 rounded-lg transition-colors"
            id="disconnect-oauth-btn"
          >
            Disconnect Account
          </button>
        </div>
      )}

      {/* Offline/Missing Config Guide */}
      {!isSandbox && !isConnected && !showDirectInput && (
        <div className="mt-6 bg-amber-950/20 border border-amber-900/40 rounded-2xl p-6" id="connection-guide-panel">
          <div className="flex items-start gap-3">
            <HelpCircle className="w-5 h-5 text-amber-500 shrink-0 mt-0.5 animate-pulse" />
            <div className="flex-1">
              <h4 className="text-sm font-bold text-amber-400 uppercase tracking-wider">OAuth Configuration Notice</h4>
              <p className="text-xs text-amber-200/70 mt-1 leading-relaxed">
                To connect to your real Google Drive, the applet requires your Google Cloud OAuth Client ID. By default, you can preview the Watchtower features instantly with high-fidelity files using <strong>Sandbox Mode</strong>.
              </p>

              <div className="mt-4 flex flex-wrap gap-3">
                <button
                  onClick={() => setShowGuide(!showGuide)}
                  className="flex items-center gap-1.5 px-4 py-2 bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 rounded-xl text-xs font-bold transition-all"
                  id="toggle-guide-btn"
                >
                  <Key className="w-3.5 h-3.5" />
                  {showGuide ? 'Hide Instructions' : 'View Setup Guide'}
                </button>
                <button
                  onClick={() => setShowDirectInput(true)}
                  className="flex items-center gap-1.5 px-4 py-2 bg-slate-900/40 text-slate-300 rounded-xl text-xs font-bold border border-slate-755 hover:bg-slate-800/40 transition-all"
                  id="show-token-input-btn"
                >
                  <Play className="w-3.5 h-3.5 text-emerald-400" />
                  Connect via Access Token
                </button>
              </div>

              {showGuide && (
                <div className="mt-4 border-t border-amber-500/10 pt-4 text-xs text-amber-200/60 space-y-2.5 leading-relaxed" id="oauth-step-by-step">
                  <p className="font-bold text-amber-400">How to authorize your workspace files:</p>
                  <ol className="list-decimal pl-4 space-y-1.5 font-mono text-[11px]">
                    <li>Go to the <a href="https://console.cloud.google.com" target="_blank" rel="noopener noreferrer" className="underline font-semibold text-amber-300 hover:text-amber-250">Google Cloud Console</a>.</li>
                    <li>Configure your OAuth Consent Screen with the scopes: <code className="bg-amber-950/60 border border-amber-900/30 px-1 rounded text-red-400">drive.readonly</code>, <code className="bg-amber-950/60 border border-amber-900/30 px-1 rounded text-red-400">spreadsheets.readonly</code>, and <code className="bg-amber-950/60 border border-amber-900/30 px-1 rounded text-red-400">documents.readonly</code>.</li>
                    <li>Create an OAuth Web Application client, and add the redirect URI <code className="bg-amber-950/60 border border-amber-900/30 px-1 rounded font-mono text-cyan-400">https://developers.google.com/oauthplayground</code> or your Dev/Prod app URL.</li>
                    <li>Paste your Client ID inside your <code className="bg-amber-950/60 border border-amber-900/30 px-1 rounded font-mono text-cyan-400">.env</code> file under <code className="bg-amber-950/60 border border-amber-900/30 px-1 rounded font-mono text-cyan-400">VITE_GOOGLE_CLIENT_ID</code>.</li>
                  </ol>
                  <div className="bg-amber-950/40 p-3.5 rounded-xl border border-amber-500/20 text-[11px] text-amber-300 mt-2 font-mono">
                    💡 <strong>Pro Tip:</strong> You can also generate a temporary Google Drive Access Token from the <a href="https://developers.google.com/oauthplayground" target="_blank" rel="noopener noreferrer" className="underline font-bold text-cyan-400 hover:text-cyan-350">Google OAuth Playground</a> to instantly authorize sync in real time without setting up any credentials!
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Direct Token Input fallback */}
      {showDirectInput && (
        <form onSubmit={handleManualTokenSubmit} className="mt-6 bg-[#05070a]/80 border border-slate-800 rounded-2xl p-5" id="token-input-form">
          <div className="flex items-start gap-3">
            <ShieldCheck className="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" />
            <div className="flex-1">
              <h4 className="text-sm font-bold text-slate-100 uppercase tracking-wider">Connect via Google Access Token</h4>
              <p className="text-xs text-slate-400 mt-1 leading-relaxed">
                Paste a Google OAuth Access Token to trigger direct real-time sync with your actual Google Drive.
              </p>

              <div className="mt-4 flex flex-col sm:flex-row gap-3">
                <input
                  type="text"
                  placeholder="ya29.a0Ac... Paste Access Token Here"
                  value={tokenInput}
                  onChange={(e) => setTokenInput(e.target.value)}
                  className="flex-1 px-4 py-2.5 bg-[#05070a] border border-slate-800 rounded-xl text-xs focus:ring-1 focus:ring-cyan-500 focus:outline-hidden font-mono text-slate-100"
                  id="direct-token-input-field"
                  required
                />
                <div className="flex gap-2">
                  <button
                    type="submit"
                    className="px-4 py-2.5 bg-cyan-600/20 hover:bg-cyan-600/30 border border-cyan-500 text-cyan-400 font-bold rounded-xl text-xs transition-all uppercase tracking-wider shrink-0"
                    id="submit-token-btn"
                  >
                    Activate Sync
                  </button>
                  <button
                    type="button"
                    onClick={() => setShowDirectInput(false)}
                    className="px-4 py-2.5 bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-400 rounded-xl text-xs font-bold transition-all uppercase tracking-wider shrink-0"
                    id="cancel-token-btn"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      )}
    </div>
  );
}
