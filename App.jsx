import React, { useState, useEffect, useRef } from 'react';

export default function App() {
  const [baseInterval, setBaseInterval] = useState(60);
  const [jitterPercent, setJitterPercent] = useState(3.6);
  const canvasRef = useRef(null);
  const [metrics, setMetrics] = useState({ avgDelta: 0, variance: 0, isAnomaly: false });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    // Support high-DPI displays
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);
    
    const width = rect.width;
    const height = rect.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    // Draw Tactical Grid
    ctx.strokeStyle = 'rgba(48, 54, 61, 0.5)';
    ctx.lineWidth = 1;
    for (let i = 0; i < width; i += 20) {
      ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, height); ctx.stroke();
    }
    for (let i = 0; i < height; i += 20) {
      ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(width, i); ctx.stroke();
    }

    // Baseline reference line
    ctx.strokeStyle = 'rgba(88, 166, 255, 0.2)';
    ctx.beginPath(); ctx.moveTo(0, height / 2); ctx.lineTo(width, height / 2); ctx.stroke();

    // Generate simulated data (20 pulses)
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

    // Draw connection pulses
    const timeScale = width / (baseInterval * numEvents);
    
    const pulseColor = jitterPercent < 5 ? '#ff7b72' : '#3fb950'; // Red for rigid/anomaly, Green for organic
    const pulseGlow = jitterPercent < 5 ? 'rgba(255, 123, 114, 0.3)' : 'rgba(63, 185, 80, 0.3)';

    events.forEach(evt => {
      const x = evt.time * timeScale;
      const y = height / 2;
      
      // Pulse height variance based on jitter
      const pulseHeight = 20 + (Math.random() * 20 * (jitterPercent/100));

      // Draw glow
      ctx.shadowBlur = 10;
      ctx.shadowColor = pulseColor;

      // Draw blip
      ctx.fillStyle = pulseColor;
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
      
      // Reset shadow
      ctx.shadowBlur = 0;

      // Draw vertical spike (simulating signal strength/event)
      ctx.strokeStyle = pulseColor;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x, y - pulseHeight);
      ctx.lineTo(x, y + pulseHeight);
      ctx.stroke();

      // Connector line to baseline
      ctx.strokeStyle = pulseGlow;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x, height);
      ctx.stroke();
    });

  }, [baseInterval, jitterPercent]);

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
          transition: all 0.3s ease;
        }
        .canvas-container { 
          margin-top: 20px; 
          border: 1px solid #30363d; 
          background: #010409; 
          border-radius: 6px; 
          overflow: hidden; 
          width: 100%; 
          display: flex; 
          justify-content: center; 
          padding: 10px; 
          box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
        }
        input[type=range] { 
          width: 100%; 
          accent-color: #58a6ff; 
          cursor: pointer;
        }
        .header-glow {
          color: #58a6ff;
          text-shadow: 0 0 10px rgba(88, 166, 255, 0.4);
          letter-spacing: 1px;
        }
      `}</style>

      <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
        <h1 className="header-glow" style={{ borderBottom: '1px solid #30363d', paddingBottom: '15px' }}>
          [WATCHTOWER] HEURISTIC UPLINK ANALYZER
        </h1>
        
        <div className="panel">
          <h3 style={{ margin: '0 0 20px 0', color: '#8b949e', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>
            Simulation Parameters
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
        </div>

        <div className="panel">
          <h3 style={{ margin: '0 0 10px 0', color: '#8b949e', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>
            Telemetry Visualization (Layer 4 Pulses)
          </h3>
          <div className="canvas-container">
            <canvas ref={canvasRef} style={{ width: '100%', height: '180px', display: 'block' }}></canvas>
          </div>
        </div>

        <div className="panel" style={{ 
          border: metrics.isAnomaly ? '1px solid #ff7b72' : '1px solid #3fb950',
          boxShadow: metrics.isAnomaly ? '0 0 20px rgba(255, 123, 114, 0.1)' : '0 0 20px rgba(63, 185, 80, 0.05)'
        }}>
          <h3 style={{ margin: '0 0 20px 0', color: '#8b949e', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>
            Diagnostic Output
          </h3>
          
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '20px' }}>
            <div style={{ background: '#010409', padding: '15px', borderRadius: '4px', border: '1px solid #30363d' }}>
              <div style={{ color: '#8b949e', fontSize: '0.8rem', marginBottom: '5px' }}>Calculated Avg Delta</div>
              <div style={{ fontSize: '1.4rem', color: '#c9d1d9' }}>{metrics.avgDelta} <span style={{fontSize: '0.9rem', color: '#8b949e'}}>sec</span></div>
            </div>
            <div style={{ background: '#010409', padding: '15px', borderRadius: '4px', border: '1px solid #30363d' }}>
              <div style={{ color: '#8b949e', fontSize: '0.8rem', marginBottom: '5px' }}>Jitter Variance (±)</div>
              <div style={{ fontSize: '1.4rem', color: '#c9d1d9' }}>{metrics.variance} <span style={{fontSize: '0.9rem', color: '#8b949e'}}>sec</span></div>
            </div>
          </div>
          
          {metrics.isAnomaly ? (
            <div style={{ 
              background: 'rgba(255, 123, 114, 0.1)', 
              padding: '16px', 
              color: '#ff7b72', 
              borderLeft: '4px solid #ff7b72',
              borderRadius: '0 4px 4px 0',
              display: 'flex',
              alignItems: 'center',
              gap: '12px'
            }}>
              <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
              <div>
                <strong>[!] ANOMALY DETECTED:</strong> Highly rigid connection intervals detected. Possible automated uplink (C2 beacon). Threshold: Jitter &lt; 5%.
              </div>
            </div>
          ) : (
            <div style={{ 
              background: 'rgba(63, 185, 80, 0.1)', 
              padding: '16px', 
              color: '#3fb950', 
              borderLeft: '4px solid #3fb950',
              borderRadius: '0 4px 4px 0',
              display: 'flex',
              alignItems: 'center',
              gap: '12px'
            }}>
              <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <div>
                <strong>[*] CLEAR:</strong> High connection variance observed. Traffic matches organic human interaction profiles.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
