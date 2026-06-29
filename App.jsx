import React, { useState, useEffect, useRef } from 'react';

export default function App() {
  // --- JITTER SIMULATION STATE ---
  const [baseInterval, setBaseInterval] = useState(60);
  const [jitterPercent, setJitterPercent] = useState(3.6);
  const jitterCanvasRef = useRef(null);
  const [metrics, setMetrics] = useState({ avgDelta: 0, variance: 0, isAnomaly: false });

  // --- SOAR PIPELINE STATE ---
  const soarCanvasRef = useRef(null);
  const [syncState, setSyncState] = useState('idle'); // idle, sweeping, parsing, healing, complete
  const [logs, setLogs] = useState([]);

  // --- JITTER CANVAS EFFECT ---
  useEffect(() => {
    const canvas = jitterCanvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);
    
    const width = rect.width;
    const height = rect.height;

    ctx.clearRect(0, 0, width, height);

    ctx.strokeStyle = 'rgba(48, 54, 61, 0.5)';
    ctx.lineWidth = 1;
    for (let i = 0; i < width; i += 20) {
      ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, height); ctx.stroke();
    }
    for (let i = 0; i < height; i += 20) {
      ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(width, i); ctx.stroke();
    }

    ctx.strokeStyle = 'rgba(88, 166, 255, 0.2)';
    ctx.beginPath(); ctx.moveTo(0, height / 2); ctx.lineTo(width, height / 2); ctx.stroke();

    const numEvents = 20;
    const events = [];
    let currentTime = 0;
    const jitterSecs = baseInterval * (jitterPercent / 100);

    let totalDelta = 0;
    for (let i = 0; i < numEvents; i++) {
      const delta = baseInterval + (Math.random() * 2 - 1) * jitterSecs;
      totalDelta += delta;
      currentTime += delta;
      events.push({ time: currentTime, delta: delta });
    }
    
    const avgDelta = totalDelta / numEvents;
    const variance = jitterSecs; 

    setMetrics({
      avgDelta: avgDelta.toFixed(2),
      variance: variance.toFixed(2),
      isAnomaly: jitterPercent < 5
    });

    const timeScale = width / (baseInterval * numEvents);
    const pulseColor = jitterPercent < 5 ? '#ff7b72' : '#3fb950'; 
    const pulseGlow = jitterPercent < 5 ? 'rgba(255, 123, 114, 0.3)' : 'rgba(63, 185, 80, 0.3)';

    events.forEach(evt => {
      const x = evt.time * timeScale;
      const y = height / 2;
      const pulseHeight = 20 + (Math.random() * 20 * (jitterPercent/100));

      ctx.shadowBlur = 10;
      ctx.shadowColor = pulseColor;
      ctx.fillStyle = pulseColor;
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.strokeStyle = pulseColor;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x, y - pulseHeight);
      ctx.lineTo(x, y + pulseHeight);
      ctx.stroke();

      ctx.strokeStyle = pulseGlow;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x, height);
      ctx.stroke();
    });
  }, [baseInterval, jitterPercent]);

  // --- SOAR CANVAS EFFECT ---
  useEffect(() => {
    const canvas = soarCanvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    
    const width = rect.width;
    const height = rect.height;
    
    let animationFrameId;
    let startTime = null;

    const render = (time) => {
      if (!startTime) startTime = time;
      const elapsed = time - startTime;
      
      ctx.save();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, width, height);

      // Grid
      ctx.strokeStyle = 'rgba(48, 54, 61, 0.5)';
      ctx.lineWidth = 1;
      for (let i = 0; i < width; i += 20) {
        ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, height); ctx.stroke();
      }
      for (let i = 0; i < height; i += 20) {
        ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(width, i); ctx.stroke();
      }

      if (syncState === 'idle') {
        ctx.fillStyle = '#8b949e';
        ctx.font = '14px "JetBrains Mono", monospace';
        ctx.fillText("[SYSTEM IDLE] AWAITING SOAR EXECUTION DIRECTIVE...", 20, 30);
      } else {
        // Node coordinates mapping
        const nodes = [
          { x: width * 0.15, y: height * 0.5, ip: '.110' },
          { x: width * 0.35, y: height * 0.3, ip: '.109' },
          { x: width * 0.55, y: height * 0.7, ip: '.112' },
          { x: width * 0.75, y: height * 0.4, ip: '.115' },
          { x: width * 0.85, y: height * 0.6, ip: '.128' },
        ];

        nodes.forEach((node, idx) => {
          let color = '#30363d'; // Offline / Unknown
          let glow = 0;
          
          if (syncState === 'sweeping') {
            const sweepX = (elapsed / 1500) * width % width;
            if (Math.abs(node.x - sweepX) < 60) {
              color = '#58a6ff'; // Scanned
              glow = 15;
            }
          } else if (syncState === 'parsing') {
            // Blinking parsing phase
            color = (Math.floor(elapsed / 150) % 2 === 0) ? '#ff7b72' : '#58a6ff'; 
            glow = 20;
          } else if (syncState === 'healing' || syncState === 'complete') {
            color = '#3fb950'; // Healthy/Synchronized
            glow = 15;
          }

          ctx.shadowBlur = glow;
          ctx.shadowColor = color;
          ctx.fillStyle = color;
          ctx.beginPath();
          ctx.arc(node.x, node.y, 6, 0, Math.PI * 2);
          ctx.fill();
          ctx.shadowBlur = 0;
          
          ctx.fillStyle = color === '#30363d' ? '#8b949e' : '#c9d1d9';
          ctx.font = '11px "JetBrains Mono", monospace';
          ctx.fillText(`IP: ${node.ip}`, node.x + 12, node.y + 4);
        });

        // Scanner Sweep Line
        if (syncState === 'sweeping') {
          const sweepX = (elapsed / 1500) * width % width;
          ctx.strokeStyle = 'rgba(88, 166, 255, 0.9)';
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(sweepX, 0);
          ctx.lineTo(sweepX, height);
          ctx.stroke();
          
          const grad = ctx.createLinearGradient(sweepX - 80, 0, sweepX, 0);
          grad.addColorStop(0, 'rgba(88, 166, 255, 0)');
          grad.addColorStop(1, 'rgba(88, 166, 255, 0.2)');
          ctx.fillStyle = grad;
          ctx.fillRect(sweepX - 80, 0, 80, height);
        }
      }
      
      ctx.restore();

      if (syncState !== 'idle') {
        animationFrameId = window.requestAnimationFrame(render);
      }
    };
    
    render(performance.now());
    
    return () => {
      window.cancelAnimationFrame(animationFrameId);
    };
  }, [syncState]);

  const triggerSync = () => {
    if (syncState !== 'idle' && syncState !== 'complete') return;
    
    setSyncState('sweeping');
    setLogs(['[+] UPLINK ESTABLISHED. EXECUTING SOAR PIPELINE...', '[*] Initiating async Nmap subnet sweep on 192.168.68.0/24...']);
    
    setTimeout(() => {
      setSyncState('parsing');
      setLogs(prev => [...prev, '[*] Parsing Nmap results and updating Watchtower_Final_Baseline.csv...']);
      
      setTimeout(() => {
        setSyncState('healing');
        setLogs(prev => [...prev, '[*] Initiating hostname resolution and healing...']);
        
        setTimeout(() => {
          setSyncState('complete');
          setLogs(prev => [...prev, '=== Mesh Synchronization Complete ===']);
          
          // Reset after a delay so it can be re-run
          setTimeout(() => {
            setSyncState('idle');
            setLogs([]);
          }, 5000);
          
        }, 2500);
      }, 2500);
    }, 3000);
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
        .canvas-container { 
          margin-top: 15px; 
          border: 1px solid #30363d; 
          background: #010409; 
          border-radius: 6px; 
          overflow: hidden; 
          width: 100%; 
          padding: 10px; 
          box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
        }
        input[type=range] { width: 100%; accent-color: #58a6ff; cursor: pointer; }
        .header-glow { color: #58a6ff; text-shadow: 0 0 10px rgba(88, 166, 255, 0.4); letter-spacing: 1px; }
        .exec-btn {
          background: #238636;
          color: white;
          border: 1px solid rgba(240,246,252,0.1);
          padding: 10px 20px;
          border-radius: 6px;
          font-family: inherit;
          font-weight: bold;
          cursor: pointer;
          transition: background 0.2s;
        }
        .exec-btn:hover { background: #2ea043; }
        .exec-btn:disabled { background: #30363d; color: #8b949e; cursor: not-allowed; }
        .log-line { margin: 5px 0; color: #c9d1d9; font-size: 0.85rem; }
        .log-line.highlight { color: #58a6ff; font-weight: bold; }
      `}</style>

      <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
        <h1 className="header-glow" style={{ borderBottom: '1px solid #30363d', paddingBottom: '15px' }}>
          [WATCHTOWER] COMMAND & CONTROL DASHBOARD
        </h1>
        
        {/* SOAR PIPELINE SIMULATOR */}
        <div className="panel" style={{ borderLeft: '4px solid #a371f7' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
            <h3 style={{ margin: 0, color: '#a371f7', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>
              SOAR Pipeline Execution (mesh_sync_skill.py)
            </h3>
            <button 
              className="exec-btn" 
              onClick={triggerSync} 
              disabled={syncState !== 'idle' && syncState !== 'complete'}
            >
              [EXECUTE] Sync Baseline
            </button>
          </div>
          
          <div style={{ display: 'flex', gap: '20px' }}>
            <div style={{ flex: 2 }}>
              <div className="canvas-container">
                <canvas ref={soarCanvasRef} style={{ width: '100%', height: '180px', display: 'block' }}></canvas>
              </div>
            </div>
            <div style={{ flex: 1, background: '#010409', border: '1px solid #30363d', borderRadius: '6px', padding: '15px', marginTop: '15px', overflowY: 'auto', maxHeight: '200px' }}>
              <div style={{ color: '#8b949e', fontSize: '0.75rem', marginBottom: '10px', textTransform: 'uppercase' }}>Pipeline Log Output</div>
              {logs.map((log, i) => (
                <div key={i} className={`log-line ${log.includes('===') ? 'highlight' : ''}`}>
                  {log}
                </div>
              ))}
              {logs.length === 0 && <div style={{ color: '#484f58', fontSize: '0.85rem' }}>Waiting for execution trigger...</div>}
            </div>
          </div>
        </div>

        {/* JITTER HEURISTIC SIMULATOR */}
        <div className="panel" style={{ borderLeft: '4px solid #58a6ff' }}>
          <h3 style={{ margin: '0 0 20px 0', color: '#58a6ff', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>
            Heuristic Uplink Analyzer (Layer 4 Pulses)
          </h3>
          <div style={{ display: 'flex', gap: '40px' }}>
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
                <span>Base Interval</span>
                <span style={{ color: '#58a6ff' }}>{baseInterval}s</span>
              </div>
              <input type="range" min="10" max="120" value={baseInterval} onChange={(e) => setBaseInterval(Number(e.target.value))} />
            </div>
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
                <span>Connection Jitter</span>
                <span style={{ color: jitterPercent < 5 ? '#ff7b72' : '#58a6ff' }}>{jitterPercent}%</span>
              </div>
              <input type="range" min="0" max="50" step="0.1" value={jitterPercent} onChange={(e) => setJitterPercent(Number(e.target.value))} />
            </div>
          </div>
          
          <div className="canvas-container">
            <canvas ref={jitterCanvasRef} style={{ width: '100%', height: '120px', display: 'block' }}></canvas>
          </div>

          <div style={{ 
            marginTop: '20px',
            padding: '16px', 
            background: metrics.isAnomaly ? 'rgba(255, 123, 114, 0.1)' : 'rgba(63, 185, 80, 0.1)',
            borderLeft: metrics.isAnomaly ? '4px solid #ff7b72' : '4px solid #3fb950',
            color: metrics.isAnomaly ? '#ff7b72' : '#3fb950',
            borderRadius: '0 4px 4px 0'
          }}>
            {metrics.isAnomaly ? (
              <strong>[!] ANOMALY DETECTED: Highly rigid connection intervals detected. Possible C2 beacon.</strong>
            ) : (
              <strong>[*] CLEAR: Traffic matches organic interaction profiles.</strong>
            )}
          </div>
        </div>

      </div>
    </div>
  );
}
