#!/usr/bin/env python3
"""
ReconForge - Automated Bug Bounty Reconnaissance Tool
Chains free OSINT tools to output comprehensive recon reports.
"""

import subprocess
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Configuration
TOOLS = {
    "subfinder": "subfinder -d {domain} -o {output}",
    "amass": "amass enum -passive -d {domain}",
    "nmap": "nmap -sV -p- -oN {output} {domain}",
    "httpx": "cat {input} | httpx -title -status-code -o {output}",
    "gau": "gau {domain}",
}

class ReconForge:
    def __init__(self, domain, output_dir="results"):
        self.domain = domain
        self.output_dir = Path(output_dir) / domain
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results = {"domain": domain, "timestamp": datetime.now().isoformat()}
    
    def run_command(self, cmd, shell=False):
        """Execute a command and return output."""
        print(f"[+] Running: {cmd[:50]}...")
        try:
            if shell:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            else:
                result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=300)
            return result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired:
            return "", "Timeout", 1
        except FileNotFoundError:
            return "", "Tool not found", 1
    
    def subdomain_enum(self):
        """Enumerate subdomains using subfinder."""
        output = self.output_dir / "subdomains.txt"
        cmd = TOOLS["subfinder"].format(domain=self.domain, output=output)
        stdout, stderr, code = self.run_command(cmd, shell=True)
        if output.exists():
            subdomains = output.read_text().strip().split("\n")
            self.results["subdomains"] = subdomains
            print(f"    Found {len(subdomains)} subdomains")
        return code == 0
    
    def port_scan(self, target=None):
        """Scan ports using nmap."""
        target = target or self.domain
        output = self.output_dir / "ports.txt"
        cmd = TOOLS["nmap"].format(domain=target, output=output)
        stdout, stderr, code = self.run_command(cmd, shell=True)
        return code == 0
    
    def http_probe(self):
        """Probe HTTP services using httpx."""
        subs_file = self.output_dir / "subdomains.txt"
        if not subs_file.exists():
            print("[-] No subdomains found, skipping HTTP probe")
            return False
        output = self.output_dir / "httpx.txt"
        cmd = TOOLS["httpx"].format(input=subs_file, output=output)
        stdout, stderr, code = self.run_command(cmd, shell=True)
        return code == 0
    
    def run(self, modules=None):
        """Run the full recon pipeline."""
        print(f"\n{'='*50}")
        print(f"ReconForge - Starting recon on {self.domain}")
        print(f"{'='*50}\n")
        
        modules = modules or ["subdomains", "ports", "http"]
        
        if "subdomains" in modules:
            self.subdomain_enum()
        
        if "ports" in modules:
            self.port_scan()
        
        if "http" in modules:
            self.http_probe()
        
        # Save final report
        report_file = self.output_dir / "report.json"
        with open(report_file, "w") as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n{'='*50}")
        print(f"Recon complete! Results saved to: {self.output_dir}")
        print(f"{'='*50}\n")
        
        return self.results

def main():
    parser = argparse.ArgumentParser(description="ReconForge - Automated Bug Bounty Recon")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    parser.add_argument("-o", "--output", default="results", help="Output directory")
    parser.add_argument("-m", "--modules", nargs="+", help="Modules to run: subdomains, ports, http")
    args = parser.parse_args()
    
    recon = ReconForge(args.domain, args.output)
    recon.run(args.modules)

if __name__ == "__main__":
    main()
