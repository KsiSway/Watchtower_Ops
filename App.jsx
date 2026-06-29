import React, { useState } from 'react';

export default function App() {
  // Nmap Module State
  const [nmapState, setNmapState] = useState('idle'); // idle, scanning, complete
  const [nmapLogs, setNmapLogs] = useState([]);
  const [nmapTarget, setNmapTarget] = useState('192.168.68.128');

  // Maigret Module State
  const [maigretState, setMaigretState] = useState('idle'); // idle, correlating, complete
  const [maigretLogs, setMaigretLogs] = useState([]);
  const [maigretTarget, setMaigretTarget] = useState('admin_target_01');

  const triggerNmap = () => {
    if (nmapState !== 'idle' && nmapState !== 'complete') return;
    setNmapState('scanning');
    setNmapLogs([`[+] INITIATING AGGRESSIVE PORT SWEEP ON TARGET: ${nmapTarget}`, '[*] Nmap 7.99 starting...']);
    
    setTimeout(() => {
      setNmapLogs(prev => [...prev, '[*] Discovered open port 22/tcp (ssh)']);
      setNmapLogs(prev => [...prev, '[*] Discovered open port 80/tcp (http) - [!] VULNERABLE TO UNENCRYPTED INTERCEPTION']);
      
      setTimeout(() => {
        setNmapLogs(prev => [...prev, '[*] OS Fingerprint: OpenWrt 22.03 (Linux 5.10)']);
        setNmapLogs(prev => [...prev, '[*] Script scanning completed.']);
        
        setTimeout(() => {
          setNmapState('complete');
          setNmapLogs(prev => [...prev, `=== NMAP SWEEP COMPLETE FOR ${nmapTarget} ===`]);
        }, 1000);
      }, 1500);
    }, 1500);
  };

  const triggerMaigret = () => {
    if (maigretState !== 'idle' && maigretState !== 'complete') return;
    setMaigretState('correlating');
    setMaigretLogs([`[+] INITIATING COGNITIVE CORRELATION FOR ALIAS: ${maigretTarget}`, '[*] Cross-referencing 3000+ platforms via Maigret engine...']);
    
    setTimeout(() => {
      setMaigretLogs(prev => [...prev, '[*] Hit: GitHub (https://github.com/admin_target_01)']);
      setMaigretLogs(prev => [...prev, '[*] Hit: Pastebin (https://pastebin.com/u/admin_target_01) - [!] Potential credential leak detected.']);
      
      setTimeout(() => {
        setMaigretLogs(prev => [...prev, '[*] Extracting PGP public keys and known BTC addresses...']);
        setMaigretLogs(prev => [...prev, '[*] Local LLM (osint_brain) synthesizing profile...']);
        
        setTimeout(() => {
          setMaigretState('complete');
          setMaigretLogs(prev => [...prev, `=== COGNITIVE CORRELATION COMPLETE FOR ${maigretTarget} ===`]);
          setMaigretLogs(prev => [...prev, '[!] PROFILE DEDUCTION: High probability of administrative access. OpSec: Moderate.']);
        }, 1500);
      }, 1500);
    }, 1500);
  };

  return (
    <div className="c2-dashboard">
      <style>{`
        * { box-sizing: border-box; }
        body { margin: 0; padding: 0; background-color: #050505; color: #c9d1d9; font-family: 'JetBrains Mono', Consolas, monospace; }
        
        .c2-dashboard { 
          min-height: 100vh; 
          padding: 3rem; 
          display: flex; 
          flex-direction: column; 
          align-items: center; 
          background: radial-gradient(circle at center, #0d1117 0%, #010409 100%);
        }
        
        .container { 
          width: 100%; 
          max-width: 1400px; 
          display: grid; 
          grid-template-columns: 1fr 1fr; 
          gap: 3rem; 
        }
        
        .header { 
          width: 100%; 
          max-width: 1400px; 
          margin-bottom: 3rem; 
          border-bottom: 1px solid #30363d; 
          padding-bottom: 1.5rem; 
        }
        
        .header-title { 
          margin: 0; 
          color: #f0f6fc; 
          font-size: 1.8rem; 
          letter-spacing: 3px; 
          text-transform: uppercase; 
          text-shadow: 0 0 15px rgba(240,246,252,0.3);
        }
        
        .header-subtitle { 
          margin: 0.5rem 0 0 0; 
          color: #8b949e; 
          font-size: 1rem; 
          letter-spacing: 1px; 
          text-transform: uppercase;
        }
        
        .module { 
          background: rgba(22, 27, 34, 0.4); 
          border: 1px solid #30363d; 
          border-radius: 10px; 
          padding: 2rem; 
          display: flex; 
          flex-direction: column;
          box-shadow: 0 8px 32px rgba(0,0,0,0.6);
          backdrop-filter: blur(10px);
        }
        
        .module-nmap { border-top: 4px solid #ff7b72; }
        .module-maigret { border-top: 4px solid #a371f7; }
        
        .module-title { 
          margin: 0 0 2rem 0; 
          font-size: 1.1rem; 
          letter-spacing: 1px; 
          text-transform: uppercase; 
        }
        .title-nmap { color: #ff7b72; }
        .title-maigret { color: #a371f7; }

        .control-group { 
          display: flex; 
          gap: 1.5rem; 
          margin-bottom: 2rem; 
        }
        
        .input-dark {
          flex: 1;
          background: #010409;
          border: 1px solid #30363d;
          color: #58a6ff;
          padding: 1rem 1.2rem;
          border-radius: 6px;
          font-family: inherit;
          font-size: 1rem;
          outline: none;
          box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
          transition: border-color 0.3s ease;
        }
        .input-dark:focus { border-color: #58a6ff; }
        
        .btn {
          padding: 1rem 2rem;
          border: none;
          border-radius: 6px;
          font-family: inherit;
          font-weight: bold;
          font-size: 1rem;
          cursor: pointer;
          transition: all 0.2s ease;
          text-transform: uppercase;
          letter-spacing: 1px;
        }
        .btn:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
        .btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; box-shadow: none; }
        .btn-nmap { background: #ff7b72; color: #010409; }
        .btn-maigret { background: #a371f7; color: #010409; }

        .status-badge {
          display: inline-flex;
          align-items: center;
          margin-bottom: 1.5rem;
          padding: 0.5rem 1rem;
          border-radius: 4px;
          font-size: 0.85rem;
          font-weight: bold;
          letter-spacing: 2px;
          animation: pulse 2s infinite;
        }
        @keyframes pulse {
          0% { opacity: 1; }
          50% { opacity: 0.6; }
          100% { opacity: 1; }
        }
        .status-scanning { background: rgba(255, 123, 114, 0.1); color: #ff7b72; border: 1px solid rgba(255, 123, 114, 0.3); }
        .status-correlating { background: rgba(163, 113, 247, 0.1); color: #a371f7; border: 1px solid rgba(163, 113, 247, 0.3); }

        .log-window {
          flex: 1;
          background: #010409;
          border: 1px solid #30363d;
          border-radius: 6px;
          padding: 1.5rem;
          overflow-y: auto;
          min-height: 400px;
          font-size: 0.9rem;
          line-height: 1.6;
          box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
        }
        
        .log-placeholder { color: #484f58; font-style: italic; }
        .log-line { margin-bottom: 0.5rem; animation: fadeIn 0.3s ease-in; }
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(5px); }
          to { opacity: 1; transform: translateY(0); }
        }
        
        .log-warning { color: #ff7b72; font-weight: bold; }
        .log-success { color: #3fb950; }
        .log-info { color: #58a6ff; font-weight: bold; }
      `}</style>

      <div className="header">
        <h1 className="header-title">[WATCHTOWER] SINGLE-VIEW ARCHITECTURE</h1>
        <p className="header-subtitle">Offensive Telemetry & Cognitive Processing Unit</p>
      </div>

      <div className="container">
        {/* NMAP MODULE */}
        <div className="module module-nmap">
          <h2 className="module-title title-nmap">Active Vulnerability Mapping (Nmap)</h2>
          <div className="control-group">
            <input 
              type="text" 
              className="input-dark" 
              value={nmapTarget} 
              onChange={(e) => setNmapTarget(e.target.value)} 
              disabled={nmapState === 'scanning'}
              placeholder="Target IP / CIDR"
            />
            <button className="btn btn-nmap" onClick={triggerNmap} disabled={nmapState === 'scanning'}>
              Execute
            </button>
          </div>
          {nmapState === 'scanning' && <div className="status-badge status-scanning">SCANNING IN PROGRESS...</div>}
          <div className="log-window">
            {nmapLogs.length === 0 && <span className="log-placeholder">System idle. Awaiting target parameters...</span>}
            {nmapLogs.map((log, i) => {
              let cls = 'log-line';
              if (log.includes('[!]')) cls += ' log-warning';
              else if (log.includes('===')) cls += ' log-info';
              else if (log.includes('[+]')) cls += ' log-success';
              return <div key={i} className={cls}>{log}</div>;
            })}
          </div>
        </div>

        {/* MAIGRET MODULE */}
        <div className="module module-maigret">
          <h2 className="module-title title-maigret">Deep Cognitive Correlation (Maigret)</h2>
          <div className="control-group">
            <input 
              type="text" 
              className="input-dark" 
              value={maigretTarget} 
              onChange={(e) => setMaigretTarget(e.target.value)} 
              disabled={maigretState === 'correlating'}
              placeholder="Target Alias / Handle"
            />
            <button className="btn btn-maigret" onClick={triggerMaigret} disabled={maigretState === 'correlating'}>
              Synthesize
            </button>
          </div>
          {maigretState === 'correlating' && <div className="status-badge status-correlating">CORRELATING ALIAS...</div>}
          <div className="log-window">
            {maigretLogs.length === 0 && <span className="log-placeholder">System idle. Awaiting alias parameters...</span>}
            {maigretLogs.map((log, i) => {
              let cls = 'log-line';
              if (log.includes('[!]')) cls += ' log-warning';
              else if (log.includes('===')) cls += ' log-info';
              else if (log.includes('[+]')) cls += ' log-success';
              return <div key={i} className={cls}>{log}</div>;
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
