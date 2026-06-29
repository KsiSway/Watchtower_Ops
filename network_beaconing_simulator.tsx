// [Environment: Docker Container Shell]
import React, { useState, useEffect, useMemo } from 'react';
import { Activity, ShieldAlert, ShieldCheck, Clock, Sliders, AlertTriangle, Terminal } from 'lucide-react';

export default function App() {
  const [baseInterval, setBaseInterval] = useState(60);
  const [jitterPercent, setJitterPercent] = useState(5);
  const [events, setEvents] = useState([]);
  
  const WINDOW_SECONDS = 600; // 10 minute window

  // Generate simulated network connection events
  useEffect(() => {
    const newEvents = [];
    let currentTime = 0;
    
    // Add initial event
    newEvents.push(0);
    
    while (currentTime < WINDOW_SECONDS) {
      // Calculate jitter variance (randomized +/- jitter percentage)
      const jitterFactor = (jitterPercent / 100);
      const variance = baseInterval * jitterFactor;
      const randomShift = (Math.random() * 2 - 1) * variance; 
      
      const delta = Math.max(1, baseInterval + randomShift); // Ensure positive time step
      currentTime += delta;
      
      if (currentTime <= WINDOW_SECONDS) {
        newEvents.push(currentTime);
      }
    }
    
    setEvents(newEvents);
  }, [baseInterval, jitterPercent]);

  // Derive Analysis Metrics
  const analysis = useMemo(() => {
    let confidenceStr = "";
    let confidenceColor = "";
    let isHighEntropy = false;

    if (jitterPercent <= 5) {
      confidenceStr = "HIGH CONFIDENCE (Automated Beacon/C2)";
      confidenceColor = "text-red-500";
    } else if (jitterPercent <= 20) {
      confidenceStr = "MODERATE (Possible Jitter Padding)";
      confidenceColor = "text-yellow-500";
    } else {
      confidenceStr = "LOW (High Entropy / Human Traffic)";
      confidenceColor = "text-emerald-500";
      isHighEntropy = true;
    }

    return { confidenceStr, confidenceColor, isHighEntropy };
  }, [jitterPercent]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 p-6 font-mono selection:bg-cyan-900">
      <div className="max-w-5xl mx-auto space-y-6">
        
        {/* Header */}
        <header className="border-b border-slate-800 pb-4 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-slate-100 flex items-center gap-2">
              <Activity className="w-6 h-6 text-cyan-500" />
              Watchtower Telemetry: Variance Simulator
            </h1>
            <p className="text-slate-400 text-sm mt-1">Mathematical Modeling of Automated Network Uplinks</p>
          </div>
          <div className="bg-slate-900 px-3 py-1.5 rounded border border-slate-800 flex items-center gap-2 text-xs text-slate-400">
            <Terminal className="w-4 h-4" />
            <span>Node: 192.168.68.128</span>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          {/* Controls Panel */}
          <div className="md:col-span-1 bg-slate-900 rounded-lg border border-slate-800 p-5 space-y-6">
            <div className="flex items-center gap-2 mb-4">
              <Sliders className="w-5 h-5 text-slate-400" />
              <h2 className="text-lg font-semibold">Parameters</h2>
            </div>

            <div className="space-y-4">
              <div>
                <div className="flex justify-between mb-1">
                  <label className="text-sm text-slate-400">Base Interval</label>
                  <span className="text-sm font-bold text-cyan-400">{baseInterval}s</span>
                </div>
                <input 
                  type="range" 
                  min="10" 
                  max="120" 
                  value={baseInterval} 
                  onChange={(e) => setBaseInterval(Number(e.target.value))}
                  className="w-full accent-cyan-500"
                />
              </div>

              <div>
                <div className="flex justify-between mb-1">
                  <label className="text-sm text-slate-400">Jitter Variance</label>
                  <span className="text-sm font-bold text-cyan-400">{jitterPercent}%</span>
                </div>
                <input 
                  type="range" 
                  min="0" 
                  max="50" 
                  value={jitterPercent} 
                  onChange={(e) => setJitterPercent(Number(e.target.value))}
                  className="w-full accent-cyan-500"
                />
              </div>
            </div>
            
            <div className="pt-4 border-t border-slate-800">
              <div className="text-xs text-slate-500 space-y-1">
                <p>[*] Window: 600s (10 min)</p>
                <p>[*] Events Plotted: {events.length}</p>
                <p>[*] Mean Delta: ~{baseInterval}s</p>
              </div>
            </div>
          </div>

          {/* Visualization & Analysis Panel */}
          <div className="md:col-span-2 space-y-6">
            
            {/* Timeline */}
            <div className="bg-slate-900 rounded-lg border border-slate-800 p-5">
              <div className="flex items-center gap-2 mb-6">
                <Clock className="w-5 h-5 text-slate-400" />
                <h2 className="text-lg font-semibold">Traffic Timeline (10 Min Window)</h2>
              </div>
              
              <div className="relative h-24 bg-slate-950 rounded border border-slate-800 overflow-hidden">
                {/* Center Line */}
                <div className="absolute top-1/2 left-0 w-full h-px bg-slate-800 -translate-y-1/2"></div>
                
                {/* Events */}
                {events.map((time, idx) => {
                  const leftPos = (time / WINDOW_SECONDS) * 100;
                  return (
                    <div 
                      key={idx}
                      className="absolute top-1/2 w-0.5 h-8 bg-cyan-500 -translate-y-1/2 shadow-[0_0_8px_rgba(6,182,212,0.8)]"
                      style={{ left: `${leftPos}%` }}
                      title={`T+${Math.round(time)}s`}
                    ></div>
                  );
                })}
              </div>
              
              <div className="flex justify-between mt-2 text-xs text-slate-500">
                <span>T+0s</span>
                <span>T+300s</span>
                <span>T+600s</span>
              </div>
            </div>

            {/* Analysis Metrics */}
            <div className="grid grid-cols-1 gap-4">
              <div className="bg-slate-900 rounded-lg border border-slate-800 p-5">
                <h3 className="text-sm text-slate-400 mb-2 uppercase tracking-wider">Automated C2 Confidence</h3>
                <div className={`text-xl font-bold flex items-center gap-2 ${analysis.confidenceColor}`}>
                  {analysis.confidenceStr.includes("HIGH") && <ShieldAlert className="w-6 h-6" />}
                  {analysis.confidenceStr.includes("MODERATE") && <AlertTriangle className="w-6 h-6" />}
                  {analysis.confidenceStr.includes("LOW") && <ShieldCheck className="w-6 h-6" />}
                  {analysis.confidenceStr}
                </div>
              </div>

              {analysis.isHighEntropy && (
                <div className="bg-emerald-950/30 border border-emerald-900 rounded-lg p-4 flex items-start gap-3">
                  <Activity className="w-5 h-5 text-emerald-500 mt-0.5 shrink-0" />
                  <div>
                    <h4 className="text-emerald-500 font-bold text-sm">ENTROPY ALERT: High Variance Detected</h4>
                    <p className="text-emerald-600/80 text-xs mt-1">
                      Traffic pattern exceeds 20% jitter threshold. Pattern is highly randomized, indicating human-driven web browsing or evasive noise generation rather than a strict programmatic beacon.
                    </p>
                  </div>
                </div>
              )}
              
              {!analysis.isHighEntropy && (
                <div className="bg-red-950/30 border border-red-900 rounded-lg p-4 flex items-start gap-3">
                  <ShieldAlert className="w-5 h-5 text-red-500 mt-0.5 shrink-0" />
                  <div>
                    <h4 className="text-red-500 font-bold text-sm">BEACON ALERT: Mathematical Rigidity Detected</h4>
                    <p className="text-red-600/80 text-xs mt-1">
                      Traffic pattern displays low entropy (var &le; 20%). Consistent connection deltas indicate a programmatic loop, characteristic of automated command-and-control (C2) or data synchronization tunnels.
                    </p>
                  </div>
                </div>
              )}
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}