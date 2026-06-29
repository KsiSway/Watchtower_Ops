import React, { useState, useEffect } from 'react';

export default function App() {
  const [activeTab, setActiveTab] = useState('mesh');
  const [apiStatus, setApiStatus] = useState('Verifying Backend Telemetry Connection...');

  // --- Initialize Live Backend Connection ---
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/status')
      .then(res => res.json())
      .then(data => setApiStatus(`[CONNECTED] Live Backend Telemetry Feed Active (${data.environment})`))
      .catch(err => setApiStatus('[OFFLINE] Live Backend Telemetry Feed Disconnected - Awaiting API Bridge.'));
  }, []);

  // --- Network Topology State ---
  const [nmapState, setNmapState] = useState('idle');
  const [nmapLogs, setNmapLogs] = useState([]);
  const [activeTarget, setActiveTarget] = useState(null);

  // --- OSINT State ---
  const [maigretState, setMaigretState] = useState('idle');
  const [maigretTarget, setMaigretTarget] = useState('');
  const [maigretLogs, setMaigretLogs] = useState([]);
  const [llmProfile, setLlmProfile] = useState(null);

  const triggerMeshSync = async () => {
    setNmapState('scanning');
    setNmapLogs(['[+] INITIATING MESH SYNCHRONIZATION...', '[*] Requesting Execution from Live Backend...']);
    
    try {
      const response = await fetch('http://127.0.0.1:8000/api/execute/mesh-sync', { method: 'POST' });
      const data = await response.json();
      
      if (response.ok) {
        setNmapLogs(prev => [...prev, ...data.output.split('\n')]);
        setNmapLogs(prev => [...prev, '=== MESH SYNCHRONIZATION COMPLETE ===']);
      } else {
        setNmapLogs(prev => [...prev, `[!] ERROR: ${data.detail}`]);
      }
    } catch (err) {
      setNmapLogs(prev => [...prev, `[!] CRITICAL ERROR: Backend Unreachable. (${err.message})`]);
    } finally {
      setNmapState('complete');
    }
  };

  const triggerNmap = async (ip) => {
    setActiveTarget(ip);
    setNmapState('scanning');
    setNmapLogs([`[+] INITIATING PERIMETER DIAGNOSTIC SCAN: ${ip}`, '[*] Transmitting parameters to Live Backend API...']);
    
    try {
      const response = await fetch('http://127.0.0.1:8000/api/execute/nmap', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ip_address: ip })
      });
      const data = await response.json();
      
      if (response.ok) {
        const lines = data.output.split('\n');
        setNmapLogs(prev => [...prev, ...lines]);
        setNmapLogs(prev => [...prev, '=== DIAGNOSTIC SCAN COMPLETE ===']);
      } else {
        setNmapLogs(prev => [...prev, `[!] ERROR: ${data.detail}`]);
      }
    } catch (err) {
      setNmapLogs(prev => [...prev, `[!] CRITICAL ERROR: Backend Unreachable. (${err.message})`]);
    } finally {
      setNmapState('complete');
    }
  };

  const triggerMaigret = () => {
    if (!maigretTarget) return;
    setMaigretState('correlating');
    setLlmProfile(null);
    setMaigretLogs([`[+] INITIATING ALIAS TELEMETRY AGGREGATION: ${maigretTarget}`, '[*] Requesting cross-reference from remote platforms...']);
    
    setTimeout(() => {
      setMaigretLogs(prev => [...prev, `[*] Hit: Software Repository (https://github.com/${maigretTarget})`]);
      setMaigretLogs(prev => [...prev, `[!] Hit: Public Paste Archive - Configuration snippet detected.`]);
      
      setTimeout(() => {
        setMaigretState('complete');
        setMaigretLogs(prev => [...prev, '=== TELEMETRY AGGREGATION COMPLETE ===']);
        setLlmProfile(`Baseline footprint analysis indicates ${maigretTarget} is engaged in technical configuration workflows. Administrative context inferred. Environmental mapping stable.`);
      }, 2000);
    }, 2000);
  };

  const nodes = [
    { ip: '192.168.68.109', host: 'S25 Edge', status: 'Nominal' },
    { ip: '192.168.68.110', host: 'OptiPlex', status: 'Nominal' },
    { ip: '192.168.68.112', host: 'Tab A8', status: 'Nominal' },
    { ip: '192.168.68.128', host: 'UNKNOWN', status: 'Anomalous' },
  ];

  return (
    <div className="c2-dashboard">
      <style>{`
        * { box-sizing: border-box; }
        body { margin: 0; padding: 0; background-color: #050505; color: #c9d1d9; font-family: 'Inter', 'JetBrains Mono', monospace; }
        
        .c2-dashboard { padding: 3rem; max-width: 1400px; margin: 0 auto; display: flex; flex-direction: column; min-height: 100vh; }
        .header-title { color: #f0f6fc; font-size: 1.6rem; text-transform: uppercase; margin: 0 0 0.5rem 0; letter-spacing: 2px; }
        
        /* Backend Telemetry Bar */
        .api-status-bar {
          background: rgba(1, 4, 9, 0.8);
          border: 1px solid #30363d;
          padding: 0.75rem 1.5rem;
          border-radius: 6px;
          font-family: 'JetBrains Mono', monospace;
          font-size: 0.85rem;
          color: #3fb950;
          margin-bottom: 2.5rem;
          display: flex;
          align-items: center;
          box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        .api-status-bar.offline { color: #8b949e; border-color: #ff7b72; }

        .tabs { display: flex; gap: 1rem; margin-bottom: 2rem; }
        .tab-btn {
          background: #010409; color: #8b949e; border: 1px solid #30363d; padding: 0.75rem 2rem; 
          border-radius: 6px; cursor: pointer; text-transform: uppercase; font-weight: bold; font-family: inherit; transition: all 0.2s; letter-spacing: 1px;
        }
        .tab-btn:hover { background: #161b22; }
        .tab-btn.active { background: #1f6feb; color: white; border-color: #1f6feb; }
        
        .panel { background: rgba(22, 27, 34, 0.5); border: 1px solid #30363d; border-radius: 10px; padding: 2.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.6); backdrop-filter: blur(10px); }
        
        .table-container { width: 100%; overflow-x: auto; border: 1px solid #30363d; border-radius: 6px; background: #010409; }
        .mesh-table { width: 100%; min-width: 850px; border-collapse: collapse; text-align: left; }
        .mesh-table th, .mesh-table td { padding: 1.25rem; border-bottom: 1px solid #30363d; white-space: nowrap; }
        .mesh-table th { color: #8b949e; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; }
        .mesh-table tr:hover { background: rgba(88, 166, 255, 0.05); }
        
        .btn-action { background: #238636; color: white; border: 1px solid rgba(240,246,252,0.1); padding: 0.6rem 1.2rem; border-radius: 6px; cursor: pointer; font-family: 'Inter', inherit; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; transition: background 0.2s; }
        .btn-action:hover:not(:disabled) { background: #2ea043; }
        .btn-action:disabled { background: #30363d; color: #8b949e; cursor: not-allowed; border-color: #30363d; }
        
        .input-dark { background: #010409; border: 1px solid #30363d; color: #58a6ff; padding: 0.85rem 1rem; border-radius: 6px; font-family: inherit; margin-right: 1rem; width: 100%; max-width: 350px; outline: none; transition: border-color 0.2s; }
        .input-dark:focus { border-color: #a371f7; }
        
        .log-window { background: #010409; border: 1px solid #30363d; border-radius: 6px; padding: 1.5rem; min-height: 250px; max-height: 500px; overflow-y: auto; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; margin-top: 1.5rem; box-shadow: inset 0 0 15px rgba(0,0,0,0.8); }
        .log-line { margin-bottom: 6px; color: #c9d1d9; line-height: 1.5; white-space: pre-wrap;}
        
        .cognitive-module { border: 1px dashed #30363d; background: rgba(1, 4, 9, 0.5); border-radius: 6px; padding: 2rem; margin-top: 1.5rem; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; min-height: 120px; }
        .cognitive-module.active { border: 1px solid #a371f7; background: rgba(163, 113, 247, 0.05); display: block; text-align: left; }
        .placeholder-text { color: #8b949e; font-style: italic; font-size: 0.95rem; }
      `}</style>

      <div>
        <h1 className="header-title">Administrative Interface</h1>
        <div className={`api-status-bar ${apiStatus.includes('OFFLINE') ? 'offline' : ''}`}>
          {apiStatus}
        </div>
      </div>

      <div className="tabs">
        <button className={`tab-btn ${activeTab === 'mesh' ? 'active' : ''}`} onClick={() => setActiveTab('mesh')}>
          Network Diagnostics
        </button>
        <button className={`tab-btn ${activeTab === 'osint' ? 'active' : ''}`} onClick={() => setActiveTab('osint')}>
          Telemetry Aggregation
        </button>
      </div>

      {activeTab === 'mesh' && (
        <div className="panel" style={{ borderTop: '4px solid #58a6ff' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <div>
              <h3 style={{ color: '#58a6ff', marginTop: 0, letterSpacing: '1px' }}>Network Topology Assessment</h3>
              <p style={{ color: '#8b949e', fontSize: '0.95rem', margin: 0 }}>Execute synchronized diagnostics via the Live Backend Telemetry Feed.</p>
            </div>
            <button className="btn-action" style={{ background: '#1f6feb' }} onClick={triggerMeshSync} disabled={nmapState === 'scanning'}>
              Synchronize Mesh
            </button>
          </div>
          
          <div className="table-container">
            <table className="mesh-table">
              <thead>
                <tr>
                  <th>IP Address</th>
                  <th>Hostname</th>
                  <th>Diagnostic State</th>
                  <th>Execution Pipeline</th>
                </tr>
              </thead>
              <tbody>
                {nodes.map(node => (
                  <tr key={node.ip}>
                    <td style={{ color: '#58a6ff', fontFamily: 'JetBrains Mono' }}>{node.ip}</td>
                    <td>{node.host}</td>
                    <td>
                      <span style={{ padding: '3px 8px', borderRadius: '4px', fontSize: '0.8rem', fontWeight: 'bold', textTransform: 'uppercase', background: node.status === 'Anomalous' ? 'rgba(255, 123, 114, 0.1)' : 'rgba(63, 185, 80, 0.1)', color: node.status === 'Anomalous' ? '#ff7b72' : '#3fb950' }}>
                        {node.status}
                      </span>
                    </td>
                    <td>
                      <button className="btn-action" onClick={() => triggerNmap(node.ip)} disabled={nmapState === 'scanning'}>
                        Initiate Scan
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
          {nmapState !== 'idle' && (
            <div className="log-window">
              <div style={{ color: '#8b949e', fontSize: '0.75rem', marginBottom: '12px', textTransform: 'uppercase', borderBottom: '1px solid #30363d', paddingBottom: '8px' }}>
                LIVE BACKEND TELEMETRY FEED {activeTarget ? `| TARGET: ${activeTarget}` : ''}
              </div>
              {nmapLogs.map((l, i) => (
                <div key={i} className="log-line" style={{ color: l.includes('ERROR') || l.includes('[!]') ? '#ff7b72' : (l.includes('===') ? '#58a6ff' : '#c9d1d9') }}>
                  {l}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {activeTab === 'osint' && (
        <div className="panel" style={{ borderTop: '4px solid #a371f7' }}>
          <h3 style={{ color: '#a371f7', marginTop: 0, letterSpacing: '1px' }}>Alias Telemetry Engine</h3>
          <p style={{ color: '#8b949e', fontSize: '0.95rem', marginBottom: '1.5rem' }}>Cross-reference target handles securely through the administrative isolated environment.</p>
          
          <div style={{ display: 'flex', alignItems: 'center', marginBottom: '2rem' }}>
            <input 
              type="text" 
              className="input-dark" 
              placeholder="Inject Target Alias"
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
              Aggregate Telemetry
            </button>
          </div>

          <div className="log-window" style={{ minHeight: '150px' }}>
             {maigretLogs.length === 0 && <div style={{ color: '#484f58', fontStyle: 'italic' }}>System idle. Awaiting alias injection parameters...</div>}
             {maigretLogs.map((l, i) => (
               <div key={i} className="log-line" style={{ color: l.includes('[!]') ? '#ff7b72' : (l.includes('===') ? '#a371f7' : '#c9d1d9') }}>
                 {l}
               </div>
             ))}
          </div>

          <h3 style={{ color: '#a371f7', marginTop: '3rem', marginBottom: '0.5rem', letterSpacing: '1px' }}>Profile Synthesis Diagnostics</h3>
          
          <div className={`cognitive-module ${llmProfile ? 'active' : ''}`}>
            {maigretState === 'idle' && (
              <span className="placeholder-text">
                [LOCKED] The logic processor requires baseline telemetry data to synthesize an environmental profile.
              </span>
            )}
            {maigretState === 'correlating' && (
              <span className="placeholder-text" style={{ color: '#a371f7', fontWeight: 'bold' }}>
                [PROCESSING] Integrating external telemetry hits into the local context window...
              </span>
            )}
            {maigretState === 'complete' && llmProfile && (
              <div>
                <div style={{ color: '#a371f7', fontSize: '0.85rem', textTransform: 'uppercase', marginBottom: '12px', fontWeight: 'bold', letterSpacing: '1px' }}>
                  Target Diagnostic Profile Generated
                </div>
                <div style={{ color: '#f0f6fc', lineHeight: 1.6, fontSize: '1rem' }}>
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
