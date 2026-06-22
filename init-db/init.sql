-- PROJECT WATCHTOWER: PostgreSQL L2 Cache Initialization
-- Target: watchtower_recon_db container

CREATE DATABASE recon_data;

\c recon_data;

-- High-Density Visual Telemetry Ledger
CREATE TABLE visual_telemetry (
    id SERIAL PRIMARY KEY,
    ingestion_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    source_ip VARCHAR(15) NOT NULL, -- Target .109 or .112
    target_label VARCHAR(100) NOT NULL,
    confidence_score NUMERIC(4, 3) NOT NULL,
    -- Utilizing INT[] instead of JSON to maintain high data density and low storage footprint
    bbox_coords INT[] NOT NULL, 
    file_path VARCHAR(255) NOT NULL,
    processed BOOLEAN DEFAULT FALSE
);

-- Indexing for high-speed dashboard retrieval
CREATE INDEX idx_source_ip ON visual_telemetry(source_ip);
CREATE INDEX idx_target_label ON visual_telemetry(target_label);
CREATE INDEX idx_ingestion_time ON visual_telemetry(ingestion_time DESC);

-- Tactical Mesh Sweeps Ledger (For future Nmap/OSINT L2 staging)
CREATE TABLE mesh_sweeps (
    id SERIAL PRIMARY KEY,
    sweep_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    node_ip VARCHAR(15) NOT NULL,
    mac_address VARCHAR(17),
    status VARCHAR(50),
    onto_serialized_data TEXT -- Storing raw ONTO/TOON columnar telemetry instead of JSON
);

CREATE INDEX idx_mesh_node ON mesh_sweeps(node_ip);
