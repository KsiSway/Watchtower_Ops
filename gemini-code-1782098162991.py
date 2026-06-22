import asyncio
import sys

async def validate_hardware_ledger(asset_map: dict, budget_ceiling: float):
    """
    Asynchronously parses infrastructure component costs and enforces financial boundary gates.
    """
    print("[*] Auditing hardware procurement ledger against authorized budget cap...")
    await asyncio.sleep(0.05)  # Simulate localized I/O lookup trace
    
    total_calculated_expenditure = sum(asset_map.values())
    margin = budget_ceiling - total_calculated_expenditure
    
    print("\n================ COST AUDIT METRICS ================")
    print(f"Target Budget Ceiling:       ${budget_ceiling:.2f}")
    print(f"Net Component Allocation:    ${total_calculated_expenditure:.2f}")
    
    if total_calculated_expenditure > budget_ceiling:
        print(f"[-] FATAL CAPITAL OVERFLOW: Budget breached by ${abs(margin):.2f}")
        return False
    
    print(f"[+] INFRASTRUCTURE LEDGER VERIFIED SECURE.")
    print(f"    - Remaining Account Liquidity Buffer: ${margin:.2f}")
    print("====================================================")
    return True

async def main():
    if sys.version_info < (3, 11):
        print("[-] FATAL: Execution requires modern Python 3.11+ async compliance.")
        sys.exit(1)

    AUTHORIZED_CEILING = 5000.00
    HARDENED_LEDGER = {
        "cpu_amd_ryzen_9_9950x3d": 899.00,
        "cooler_noctua_nh_d15_g2": 150.00,
        "motherboard_msi_x870e_tomahawk": 329.00,
        "gpu_nvidia_rtx_5080_16gb_new": 1250.00,
        "ram_64gb_ddr5_6000_qvl": 945.00,
        "storage_dual_samsung_990pro_4tb_total": 738.00,
        "psu_seasonic_prime_1000w_titanium": 180.00,
        "chassis_fractal_torrent_steel": 200.00
    }
    
    await validate_hardware_ledger(HARDENED_LEDGER, AUTHORIZED_CEILING)

if __name__ == "__main__":
    asyncio.run(main())