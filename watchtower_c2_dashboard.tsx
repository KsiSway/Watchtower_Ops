// [Environment: Docker Container Shell]
import React, { useState } from 'react';
import { Terminal, Activity, Network, Target, ShieldAlert, Cpu, HardDrive, Server, Play, AlertOctagon } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('mesh');
  const [terminalLog, setTerminalLog] = useState([
    "[*] Watchtower C2 Initialized.",
    "[*] Environment: Docker Container (Node 24.15.0)",
    "[*] Memory RSS: 112.80 MB | Status: Optimal",
    "[*] Awaiting Operator directive..."
  ]);

  const runCommand = (cmd) => {
    setTerminalLog(prev => [...prev, `(.venv) PS D:\\Watchtower_Ops> ${cmd}`, "[*] Executing payload... awaiting telemetry."]);
  };

  const meshNodes = [
    { ip: "192.168.68.1", host: "Deco_XE75_Gateway", status: "Clear" },
    { ip: "192.168.68.104", host: "Xbox_Series_S", status: "Clear" },
    { ip: "192.168.68.109", host: "S25_Edge_Commander", status: "Active" },
    { ip: "192.168.68.110", host: "OptiPlex_Host", status: "Active" },
    { ip: "192.168.68.128", host: "Mango_Router", status: "Segmented" }
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-300 font-mono flex flex-col selection:bg-cyan-900">
      {/* Header */}
      <header className="bg-slate-900 border-b border-slate-800 p-4 flex justify-between items-center">
        <div className="flex items-center gap-3">
          <ShieldAlert className="text-cyan-500 w-6 h-6" />
          <h1 className="text-xl font-bold tracking-widest text-slate-100">WATCHTOWER<span className="text-cyan-500">_C2</span></h1>
        </div>
        <div className="flex gap-4 text-xs text-slate-400">
          <div className="flex items-center gap-1"><Activity className="w-4 h-4 text-emerald-500" /> SYSTEM: NOMINAL</div>
          <div className="flex items-center gap-1"><Cpu className="w-4 h-4" /> RAM: 112.8 MB</div>
        </div>
      </header>

      {/* Main Layout */}
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <div className="w-64 bg-slate-900 border-r border-slate-800 p-4 flex flex-col gap-2">
          <button 
            onClick={() => setActiveTab('mesh')}
            className={`flex items-center gap-3 p-3 rounded text-sm transition-colors ${activeTab === 'mesh' ? 'bg-cyan-950/50 text-cyan-400 border border-cyan-900' : 'hover:bg-slate-800'}`}
          >
            <Network className="w-4 h-4" /> Mesh Telemetry
          </button>
          <button 
            onClick={() => setActiveTab('osint')}
            className={`flex items-center gap-3 p-3 rounded text-sm transition-colors ${activeTab === 'osint' ? 'bg-cyan-950/50 text-cyan-400 border border-cyan-900' : 'hover:bg-slate-800'}`}
          >
            <Target className="w-4 h-4" /> OSINT Engine
          </button>
          <button 
            onClick={() => setActiveTab('alerts')}
            className={`flex items-center gap-3 p-3 rounded text-sm transition-colors ${activeTab === 'alerts' ? 'bg-cyan-950/50 text-cyan-400 border border-cyan-900' : 'hover:bg-slate-800'}`}
          >
            <AlertOctagon className="w-4 h-4" /> Active Alerts
          </button>
        </div>

        {/* Content Area */}
        <div className="flex-1 flex flex-col p-6 gap-6 overflow-y-auto">
          
          {/* OSINT Tab */}
          {activeTab === 'osint' && (
            <div className="space-y-4">
              <h2 className="text-lg font-bold text-slate-100 border-b border-slate-800 pb-2">Offensive Reconnaissance & OSINT</h2>
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-slate-900 p-4 rounded border border-slate-800">
                  <h3 className="text-cyan-500 font-bold mb-2">recon_core.py</h3>
                  <p className="text-xs text-slate-400 mb-4">Core intelligence engine. Aggregates data from peripheral modules and initiates Shodan/Censys API sweeps.</p>
                  <button onClick={() => runCommand('python osint_brain.py "telemetry"')} className="bg-slate-800 hover:bg-cyan-900 text-xs px-3 py-2 rounded flex items-center gap-2 border border-slate-700 hover:border-cyan-500 transition-all">
                    <Play className="w-3 h-3" /> Execute Engine
                  </button>
                </div>
                <div className="bg-slate-900 p-4 rounded border border-slate-800">
                  <h3 className="text-emerald-500 font-bold mb-2">osint_sherlock.py</h3>
                  <p className="text-xs text-slate-400 mb-4">Tactical wrapper for high-velocity username sweeps across 300+ platforms. Returns positive hits only.</p>
                  <button onClick={() => runCommand('python osint_sherlock.py --target "karenaki"')} className="bg-slate-800 hover:bg-emerald-900 text-xs px-3 py-2 rounded flex items-center gap-2 border border-slate-700 hover:border-emerald-500 transition-all">
                    <Play className="w-3 h-3" /> Hunt Alias
                  </button>
                </div>
                <div className="bg-slate-900 p-4 rounded border border-slate-800">
                  <h3 className="text-purple-500 font-bold mb-2">osint_tor_fetcher.py</h3>
                  <p className="text-xs text-slate-400 mb-4">Async Tor-routed crawler with regex-based IOC extraction (BTC/XMR/PGP/Email).</p>
                  <button onClick={() => runCommand('python osint_tor_fetcher.py')} className="bg-slate-800 hover:bg-purple-900 text-xs px-3 py-2 rounded flex items-center gap-2 border border-slate-700 hover:border-purple-500 transition-all">
                    <Play className="w-3 h-3" /> Initiate Fetch
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Mesh Tab */}
          {activeTab === 'mesh' && (
            <div className="space-y-4">
              <div className="flex justify-between items-end border-b border-slate-800 pb-2">
                <h2 className="text-lg font-bold text-slate-100">Local Mesh Topology (192.168.68.x)</h2>
                <button onClick={() => runCommand('python mesh_sync_skill.py')} className="text-xs bg-slate-800 px-3 py-1.5 rounded border border-slate-700 hover:bg-slate-700 flex items-center gap-2">
                  <Network className="w-3 h-3" /> Sync Baseline
                </button>
              </div>
              <div className="bg-slate-900 rounded border border-slate-800 overflow-hidden">
                <table className="w-full text-sm text-left">
                  <thead className="bg-slate-950 text-slate-400">
                    <tr>
                      <th className="px-4 py-3 font-medium">IP Address</th>
                      <th className="px-4 py-3 font-medium">Hostname</th>
                      <th className="px-4 py-3 font-medium">State</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800">
                    {meshNodes.map((node, i) => (
                      <tr key={i} className="hover:bg-slate-800/50">
                        <td className="px-4 py-3 font-mono text-cyan-400">{node.ip}</td>
                        <td className="px-4 py-3">{node.host}</td>
                        <td className="px-4 py-3">
                          <span className={`px-2 py-1 rounded text-xs ${node.status === 'Clear' ? 'bg-emerald-950 text-emerald-400' : node.status === 'Segmented' ? 'bg-red-950 text-red-400' : 'bg-cyan-950 text-cyan-400'}`}>
                            {node.status}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Alerts Tab */}
          {activeTab === 'alerts' && (
            <div className="space-y-4">
              <h2 className="text-lg font-bold text-slate-100 border-b border-slate-800 pb-2">Active Alerts Ledger</h2>
              <div className="bg-red-950/20 border border-red-900/50 p-4 rounded flex gap-4 items-start">
                <ShieldAlert className="w-6 h-6 text-red-500 shrink-0" />
                <div>
                  <h3 className="text-red-400 font-bold mb-1">baseline_variance_event</h3>
                  <p className="text-sm text-slate-300 mb-2">Source Node: 192.168.68.128 | Jitter: 3.6% | Confidence: HIGH</p>
                  <p className="text-xs text-slate-400 font-mono bg-slate-950 p-2 rounded border border-slate-800">
                    "status": "pending_analysis", "target": "192.168.8.241", "endpoints": ["140.82.121.3", "34.54.84.110"]
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Persistent Terminal */}
          <div className="mt-auto pt-6 border-t border-slate-800">
            <div className="bg-slate-950 border border-slate-800 rounded p-4 h-48 overflow-y-auto font-mono text-xs">
              <div className="flex items-center gap-2 mb-2 pb-2 border-b border-slate-900 text-slate-500">
                <Terminal className="w-4 h-4" /> Watchtower Ops Terminal
              </div>
              {terminalLog.map((log, i) => (
                <div key={i} className={`mb-1 ${log.startsWith('(.venv)') ? 'text-cyan-500' : log.startsWith('[!]') ? 'text-red-500' : 'text-slate-400'}`}>
                  {log}
                </div>
              ))}
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}