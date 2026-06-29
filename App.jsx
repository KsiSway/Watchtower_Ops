import React, { useState } from 'react';

export default function App() {
  const [nmapState, setNmapState] = useState('idle'); // idle, scanning, complete
  const [nmapLogs, setNmapLogs] = useState([]);
  const [nmapTarget, setNmapTarget] = useState('192.168.68.128');

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
        }, 1500);
      }, 2000);
    }, 2000);
  };

  const triggerMaigret = () => {
    if (maigretState !== 'idle' && maigretState !== 'complete') return;
    
    setMaigretState('correlating');
    setMaigretLogs([`[+] INITIATING COGNITIVE CORRELATION FOR ALIAS: ${maigretTarget}`, '[*] Cross-referencing 3000+ platforms via Maigret engine...']);
    
    setTimeout(() => {
      setMaigretLogs(prev => [...prev, '[*] Hit: GitHub (https://github.com/admin_target_01)']);
      setMaigretLogs(prev => [...prev, '[*] Hit: Pastebin (https://pastebin.com/u/admin_target_01) - Potential credential leak detected.']);
      
      setTimeout(() => {
        setMaigretLogs(prev => [...prev, '[*] Extracting PGP public keys and known BTC addresses...']);
        setMaigretLogs(prev => [...prev, '[*] Local LLM (osint_brain) synthesizing profile...']);
        
        setTimeout(() => {
          setMaigretState('complete');
          setMaigretLogs(prev => [...prev, `=== COGNITIVE CORRELATION COMPLETE FOR ${maigretTarget} ===`]);
          setMaigretLogs(prev => [...prev, 'PROFILE DEDUCTION: High probability of administrative access. OpSec: Moderate.']);
        }, 2000);
      }, 2500);
    }, 2500);
  };

  return (
    <div style={{ backgroundColor: '#0d1117', color: '#c9d1d9', fontFamily: '"JetBrains Mono", Consolas, monospace', minHeight: '100vh', padding: '2rem' }}>
      <style>{`
        .panel { 
          background: rgba(22, 27, 34, 0.7); 
          border: 1px solid #30363d; 
          border-radius: 8px; 
          padding: 24px; 
          box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4); 
          backdrop-filter: blur(10px);
          margin-bottom: 24px;
        }
        .header-glow { color: #ff7b72; text-shadow: 0 0 10px rgba(255, 123, 114, 0.4); letter-spacing: 1px; }
        .module-title { margin: 0 0 15px 0; text-transform: uppercase; fontSize: 0.9rem; letterSpacing: 1px; }
        .input-dark {
          background: #010409;
          border: 1px solid #30363d;
          color: #c9d1d9;
          padding: 8px 12px;
          border-radius: 6px;
          font-family: inherit;
          width: 250px;
          margin-right: 15px;
        }
        .exec-btn {
          background: #238636;
          color: white;
          border: 1px solid rgba(240,246,252,0.1);
          padding: 8px 16px;
          border-radius: 6px;
          font-family: inherit;
          font-weight: bold;
          cursor: pointer;
          transition: background 0.2s;
        }
        .exec-btn:hover { background: #2ea043; }
        .exec-btn:disabled { background: #30363d; color: #8b949e; cursor: not-allowed; }
        .log-container {
          background: #010409; 
          border: 1px solid #30363d; 
          border-radius: 6px; 
          padding: 15px; 
          margin-top: 20px; 
          overflow-y: auto; 
          min-height: 150px;
        }
        .log-line { margin: 5px 0; color: #c9d1d9; font-size: 0.85rem; }
        .log-line.warning { color: #ff7b72; font-weight: bold; }
        .log-line.success { color: #3fb950; font-weight: bold; }
        .log-line.info { color: #58a6ff; font-weight: bold; }
      `}</style>

      <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
        <h1 className="header-glow" style={{ borderBottom: '1px solid #30363d', paddingBottom: '15px' }}>
          [WATCHTOWER] ACTIVE OFFENSIVE TELEMETRY
        </h1>

        {/* NMAP VULNERABILITY MAPPING */}
        <div className="panel" style={{ borderLeft: '4px solid #ff7b72' }}>
          <h3 className="module-title" style={{ color: '#ff7b72' }}>Active Vulnerability Mapping (Nmap)</h3>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <input 
              type="text" 
              className="input-dark" 
              value={nmapTarget} 
              onChange={(e) => setNmapTarget(e.target.value)} 
              disabled={nmapState === 'scanning'}
            />
            <button 
              className="exec-btn" 
              onClick={triggerNmap} 
              disabled={nmapState === 'scanning'}
            >
              [EXECUTE] Deep Port Sweep
            </button>
            {nmapState === 'scanning' && <span style={{ marginLeft: '15px', color: '#ff7b72' }}>SCANNING...</span>}
          </div>
          
          <div className="log-container">
            {nmapLogs.length === 0 && <div style={{ color: '#484f58', fontSize: '0.85rem' }}>Waiting for target execution...</div>}
            {nmapLogs.map((log, i) => {
              let cls = 'log-line';
              if (log.includes('[!]')) cls += ' warning';
              if (log.includes('===')) cls += ' info';
              return <div key={i} className={cls}>{log}</div>;
            })}
          </div>
        </div>

        {/* MAIGRET COGNITIVE CORRELATION */}
        <div className="panel" style={{ borderLeft: '4px solid #a371f7' }}>
          <h3 className="module-title" style={{ color: '#a371f7' }}>Deep Cognitive Correlation (Maigret + LLM)</h3>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <input 
              type="text" 
              className="input-dark" 
              value={maigretTarget} 
              onChange={(e) => setMaigretTarget(e.target.value)} 
              disabled={maigretState === 'correlating'}
            />
            <button 
              className="exec-btn" 
              onClick={triggerMaigret} 
              disabled={maigretState === 'correlating'}
            >
              [EXECUTE] Synthesize Alias
            </button>
            {maigretState === 'correlating' && <span style={{ marginLeft: '15px', color: '#a371f7' }}>CORRELATING...</span>}
          </div>
          
          <div className="log-container">
            {maigretLogs.length === 0 && <div style={{ color: '#484f58', fontSize: '0.85rem' }}>Waiting for alias input...</div>}
            {maigretLogs.map((log, i) => {
              let cls = 'log-line';
              if (log.includes('PROFILE DEDUCTION')) cls += ' success';
              if (log.includes('===')) cls += ' info';
              return <div key={i} className={cls}>{log}</div>;
            })}
          </div>
        </div>

      </div>
    </div>
  );
}
