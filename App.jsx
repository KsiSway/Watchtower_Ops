import React, { useState } from 'react';

export default function App() {
  const [activeTab, setActiveTab] = useState('mesh');

  // --- Nmap State ---
  const [nmapState, setNmapState] = useState('idle');
  const [nmapLogs, setNmapLogs] = useState([]);
  const [activeTarget, setActiveTarget] = useState(null);

  // --- OSINT State ---
  const [maigretState, setMaigretState] = useState('idle');
  const [maigretTarget, setMaigretTarget] = useState('');
  const [maigretLogs, setMaigretLogs] = useState([]);
  const [llmProfile, setLlmProfile] = useState(null);

  const triggerNmap = (ip) => {
    setActiveTarget(ip);
    setNmapState('scanning');
    setNmapLogs([`[+] INITIATING AGGRESSIVE PORT SWEEP ON TARGET: ${ip}`, '[*] Nmap 7.99 starting...']);
    
    setTimeout(() => {
      setNmapLogs(prev => [...prev, '[*] Discovered open port 22/tcp (ssh)']);
      setNmapLogs(prev => [...prev, '[!] Discovered open port 80/tcp (http) - VULNERABLE TO UNENCRYPTED INTERCEPTION']);
      
      setTimeout(() => {
        setNmapLogs(prev => [...prev, '[*] OS Fingerprint: OpenWrt 22.03']);
        setNmapState('complete');
        setNmapLogs(prev => [...prev, '=== NMAP SWEEP COMPLETE ===']);
      }, 1500);
    }, 1500);
  };

  const triggerMaigret = () => {
    if (!maigretTarget) return;
    setMaigretState('correlating');
    setLlmProfile(null);
    setMaigretLogs([`[+] INITIATING MAIGRET SCAN FOR ALIAS: ${maigretTarget}`, '[*] Cross-referencing 3000+ platforms...']);
    
    setTimeout(() => {
      setMaigretLogs(prev => [...prev, `[*] Hit: GitHub (https://github.com/${maigretTarget})`]);
      setMaigretLogs(prev => [...prev, `[!] Hit: Pastebin - Potential credential leak detected for ${maigretTarget}.`]);
      
      setTimeout(() => {
        setMaigretState('complete');
        setMaigretLogs(prev => [...prev, '=== MAIGRET SCAN COMPLETE ===']);
        setLlmProfile(`Based on the footprint across GitHub and developer forums, ${maigretTarget} has a high probability of administrative access. Technical background in DevOps. OpSec is currently evaluated as Moderate. Secondary aliases detected on Tor hidden services.`);
      }, 2000);
    }, 2000);
  };

  const nodes = [
    { ip: '192.168.68.109', host: 'S25 Edge', status: 'Clear' },
    { ip: '192.168.68.110', host: 'OptiPlex', status: 'Clear' },
    { ip: '192.168.68.112', host: 'Tab A8', status: 'Clear' },
    { ip: '192.168.68.128', host: 'UNKNOWN', status: 'Anomalous' },
  ];

  return (
    <div className="c2-dashboard">
      <style>{`
        * { box-sizing: border-box; }
        body { margin: 0; padding: 0; background-color: #050505; color: #c9d1d9; font-family: 'JetBrains Mono', Consolas, monospace; }
        
        .c2-dashboard { padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .header-title { color: #58a6ff; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 2rem; border-bottom: 1px solid #30363d; padding-bottom: 1rem; text-shadow: 0 0 10px rgba(88,166,255,0.4); }
        
        .tabs { display: flex; gap: 1rem; margin-bottom: 2rem; }
        .tab-btn {
          background: #010409; 
          color: #8b949e; 
          border: 1px solid #30363d; 
          padding: 0.75rem 1.5rem; 
          border-radius: 4px; 
          cursor: pointer; 
          text-transform: uppercase; 
          font-weight: bold; 
          font-family: inherit;
          transition: all 0.2s;
        }
        .tab-btn:hover { background: #161b22; }
        .tab-btn.active { background: #1f6feb; color: white; border-color: #1f6feb; }
        
        .panel { 
          background: rgba(22, 27, 34, 0.5); 
          border: 1px solid #30363d; 
          border-radius: 8px; 
          padding: 2rem; 
          margin-bottom: 2rem; 
          box-shadow: 0 4px 20px rgba(0,0,0,0.5);
          backdrop-filter: blur(5px);
        }
        
        /* MESH TAB CSS FIXES */
        .table-container {
          width: 100%;
          overflow-x: auto; /* CRITICAL FIX: Ensures the table can scroll horizontally on small screens */
          border: 1px solid #30363d;
          border-radius: 4px;
          background: #010409;
        }
        .mesh-table {
          width: 100%;
          min-width: 800px; /* Forces scroll on small viewports so the far right column is never clipped */
          border-collapse: collapse;
          text-align: left;
        }
        .mesh-table th, .mesh-table td { padding: 1rem; border-bottom: 1px solid #30363d; white-space: nowrap; }
        .mesh-table th { color: #8b949e; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; }
        .mesh-table tr:last-child td { border-bottom: none; }
        .mesh-table tr:hover { background: rgba(88, 166, 255, 0.05); }
        
        .btn-action { 
          background: #238636; 
          color: white; 
          border: 1px solid rgba(240,246,252,0.1); 
          padding: 0.5rem 1rem; 
          border-radius: 4px; 
          cursor: pointer; 
          font-family: inherit;
          font-weight: bold;
          text-transform: uppercase;
        }
        .btn-action:hover:not(:disabled) { background: #2ea043; }
        .btn-action:disabled { background: #30363d; color: #8b949e; cursor: not-allowed; }
        
        /* OSINT TAB CSS FIXES */
        .input-dark { 
          background: #010409; 
          border: 1px solid #30363d; 
          color: #58a6ff; 
          padding: 0.75rem 1rem; 
          border-radius: 4px; 
          font-family: inherit; 
          margin-right: 1rem; 
          width: 100%;
          max-width: 300px; 
          outline: none;
        }
        .input-dark:focus { border-color: #a371f7; }
        
        .log-window { 
          background: #010409; 
          border: 1px solid #30363d; 
          border-radius: 4px; 
          padding: 1rem; 
          min-height: 150px; 
          overflow-y: auto; 
          font-size: 0.85rem; 
          margin-top: 1rem; 
          box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
        }
        .log-line { margin-bottom: 5px; color: #c9d1d9; }
        
        /* COGNITIVE CORRELATION VISUAL PLACEHOLDER */
        .cognitive-module {
          border: 1px dashed #30363d;
          background: rgba(1, 4, 9, 0.5);
          border-radius: 4px;
          padding: 2rem;
          margin-top: 1rem;
          transition: all 0.3s ease;
          display: flex;
          align-items: center;
          justify-content: center;
          min-height: 100px;
        }
        .cognitive-module.active {
          border: 1px solid #a371f7;
          background: rgba(163, 113, 247, 0.05);
          display: block;
          text-align: left;
        }
        .placeholder-text { color: #8b949e; font-style: italic; font-size: 0.9rem; }
      `}</style>

      <h1 className="header-title">[WATCHTOWER] COMMAND & CONTROL</h1>

      <div className="tabs">
        <button className={`tab-btn ${activeTab === 'mesh' ? 'active' : ''}`} onClick={() => setActiveTab('mesh')}>
          Mesh Intelligence
        </button>
        <button className={`tab-btn ${activeTab === 'osint' ? 'active' : ''}`} onClick={() => setActiveTab('osint')}>
          OSINT Engine
        </button>
      </div>

      {activeTab === 'mesh' && (
        <div className="panel" style={{ borderTop: '4px solid #58a6ff' }}>
          <h3 style={{ color: '#58a6ff', marginTop: 0, letterSpacing: '1px' }}>Network Topology</h3>
          <p style={{ color: '#8b949e', fontSize: '0.9rem', marginBottom: '1.5rem' }}>Active nodes detected via mesh_sync_skill.py. Execute targeted port sweeps to identify unencrypted vectors.</p>
          
          <div className="table-container">
            <table className="mesh-table">
              <thead>
                <tr>
                  <th>IP Address</th>
                  <th>Hostname</th>
                  <th>Status</th>
                  <th>Perimeter Scan (Nmap)</th>
                </tr>
              </thead>
              <tbody>
                {nodes.map(node => (
                  <tr key={node.ip}>
                    <td style={{ color: '#58a6ff' }}>{node.ip}</td>
                    <td>{node.host}</td>
                    <td>
                      <span style={{ 
                        padding: '2px 6px', 
                        borderRadius: '3px', 
                        fontSize: '0.75rem', 
                        fontWeight: 'bold',
                        textTransform: 'uppercase',
                        background: node.status === 'Anomalous' ? 'rgba(255, 123, 114, 0.1)' : 'rgba(63, 185, 80, 0.1)',
                        color: node.status === 'Anomalous' ? '#ff7b72' : '#3fb950' 
                      }}>
                        {node.status}
                      </span>
                    </td>
                    <td>
                      <button 
                        className="btn-action" 
                        onClick={() => triggerNmap(node.ip)}
                        disabled={nmapState === 'scanning'}
                      >
                        [EXECUTE] Port Sweep
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
          {nmapState !== 'idle' && (
            <div className="log-window" style={{ marginTop: '2rem' }}>
              <div style={{ color: '#8b949e', fontSize: '0.75rem', marginBottom: '10px', textTransform: 'uppercase' }}>
                NMAP TELEMETRY: {activeTarget}
              </div>
              {nmapLogs.map((l, i) => (
                <div key={i} className="log-line" style={{ 
                  color: l.includes('[!]') ? '#ff7b72' : (l.includes('===') ? '#58a6ff' : '#c9d1d9'),
                  fontWeight: l.includes('[!]') || l.includes('===') ? 'bold' : 'normal'
                }}>
                  {l}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {activeTab === 'osint' && (
        <div className="panel" style={{ borderTop: '4px solid #a371f7' }}>
          <h3 style={{ color: '#a371f7', marginTop: 0, letterSpacing: '1px' }}>Maigret Interrogation Engine</h3>
          <p style={{ color: '#8b949e', fontSize: '0.9rem', marginBottom: '1.5rem' }}>Cross-reference target handles against 3000+ known platforms to feed the Local LLM cognitive pipeline.</p>
          
          <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1.5rem' }}>
            <input 
              type="text" 
              className="input-dark" 
              placeholder="Target Alias / Handle"
              value={maigretTarget}
              onChange={e => setMaigretTarget(e.target.value)}
              disabled={maigretState === 'correlating'}
            />
            <button 
              className="btn-action" 
              style={{ background: '#a371f7', color: '#010409' }}
              onClick={triggerMaigret}
              disabled={maigretState === 'correlating' || !maigretTarget}
            >
              [EXECUTE] Maigret Scan
            </button>
          </div>

          <div className="log-window" style={{ minHeight: '120px' }}>
             {maigretLogs.length === 0 && <div style={{ color: '#484f58', fontStyle: 'italic' }}>System idle. Awaiting alias parameter injection...</div>}
             {maigretLogs.map((l, i) => (
               <div key={i} className="log-line" style={{ 
                 color: l.includes('[!]') ? '#ff7b72' : (l.includes('===') ? '#a371f7' : '#c9d1d9'),
                 fontWeight: l.includes('[!]') || l.includes('===') ? 'bold' : 'normal'
               }}>
                 {l}
               </div>
             ))}
          </div>

          <h3 style={{ color: '#a371f7', marginTop: '2.5rem', marginBottom: '0.5rem', letterSpacing: '1px' }}>Cognitive Correlation (Local LLM)</h3>
          
          <div className={`cognitive-module ${llmProfile ? 'active' : ''}`}>
            {maigretState === 'idle' && (
              <span className="placeholder-text">
                [LOCKED] The OSINT Brain requires Maigret baseline data to synthesize a profile. Execute a scan above to unlock this module.
              </span>
            )}
            {maigretState === 'correlating' && (
              <span className="placeholder-text" style={{ color: '#a371f7', fontWeight: 'bold' }}>
                [PROCESSING] Integrating Maigret hits into Local LLM context window...
              </span>
            )}
            {maigretState === 'complete' && llmProfile && (
              <div>
                <div style={{ color: '#a371f7', fontSize: '0.85rem', textTransform: 'uppercase', marginBottom: '12px', fontWeight: 'bold', letterSpacing: '1px' }}>
                  Target Profile Deduction Generated
                </div>
                <div style={{ color: '#f0f6fc', lineHeight: 1.6, fontSize: '0.95rem' }}>
                  {llmProfile}
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
