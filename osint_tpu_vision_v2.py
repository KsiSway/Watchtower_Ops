#!/usr/bin/env python3
# PROJECT WATCHTOWER: Edge TPU -> PostgreSQL Bridge (V2.2 Thread-Safe)
# Architecture: OptiPlex x64 Host -> Google Coral TPU -> Postgres L2 Cache

import os
import time
import asyncio
import psycopg2
import shutil
from PIL import Image
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import detect

# --- TACTICAL CONFIGURATION ---
STAGING_DIR = "D:/Watchtower_Ops/Payloads/Visual_Intel"
ARCHIVE_DIR = "D:/Watchtower_Ops/Payloads/Visual_Intel_Analyzed"
MODEL_PATH = "D:/Watchtower_Ops/Models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite"
LABEL_PATH = "D:/Watchtower_Ops/Models/coco_labels.txt"

DB_PARAMS = {
    "dbname": "recon_data",
    "user": "watchtower_admin",
    "password": "watchtower_secure_2026",
    "host": "localhost",
    "port": "5432"
}

def inject_telemetry(source_ip, label, score, bbox, filepath):
    """Synchronous DB injection designed for threaded offloading."""
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    
    bbox_array = [int(bbox.xmin), int(bbox.ymin), int(bbox.xmax), int(bbox.ymax)]
    
    query = """
        INSERT INTO visual_telemetry 
        (source_ip, target_label, confidence_score, bbox_coords, file_path)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (source_ip, label, float(score), bbox_array, filepath))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True

async def process_frame(interpreter, labels, filepath):
    try:
        image = Image.open(filepath).convert('RGB')
        _, scale = common.set_resized_input(
            interpreter, image.size, lambda size: image.resize(size, Image.LANCZOS))

        start_time = time.perf_counter()
        interpreter.invoke()
        inference_time = time.perf_counter() - start_time

        objs = detect.get_objects(interpreter, score_threshold=0.5, image_scale=scale)
        filename = os.path.basename(filepath)
        source_ip = "192.168.68.109" if "109" in filename else "192.168.68.112"
        db_success = False

        if objs:
            print(f"[+] Detected {len(objs)} target signatures in {inference_time:.3f}s")
            for obj in objs:
                label = labels.get(obj.id, obj.id)
                print(f"    -> TARGET: {label} | CONFIDENCE: {obj.score:.2f} | DB: INJECTING")
                
                # Thread-safe L2 Cache Injection
                db_success = await asyncio.to_thread(
                    inject_telemetry, source_ip, label, obj.score, obj.bbox, filepath
                )
        else:
            print(f"[*] {filename} STATUS: CLEAR")
            db_success = True # No objects, but processing succeeded

        # Idempotent Archiving
        if db_success:
            shutil.move(filepath, os.path.join(ARCHIVE_DIR, filename))

    except Exception as e:
        print(f"[!] INFERENCE/DB FAILURE on {filepath}: {e}")

async def watch_airlock():
    print("[*] INITIALIZING EDGE TPU DB BRIDGE (V2.2 THREAD-SAFE)...")
    os.makedirs(STAGING_DIR, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    try:
        interpreter = edgetpu.make_interpreter(MODEL_PATH)
        interpreter.allocate_tensors()
        labels = dataset.read_label_file(LABEL_PATH) if os.path.exists(LABEL_PATH) else {}
        print("[+] TPU HARDWARE BINDING SECURED. Awaiting optical payloads...")
    except Exception as e:
        print(f"[!] CRITICAL: TPU BINDING FAILED. Verify USBIPD persistence. Details: {e}")
        return

    while True:
        payloads = [os.path.join(STAGING_DIR, f) for f in os.listdir(STAGING_DIR) if f.endswith('.png')]
        for payload in payloads:
            await process_frame(interpreter, labels, payload)
        
        await asyncio.sleep(1.5)

if __name__ == '__main__':
    try:
        asyncio.run(watch_airlock())
    except KeyboardInterrupt:
        print("\n[*] TPU VISION ENGINE OFFLINE. Severing bindings.")
