# ReconForge - Automated Bug Bounty Recon Tool

ReconForge is an automated reconnaissance framework designed for bug bounty hunters and security researchers. It streamlines the initial information gathering phase by chaining multiple OSINT and network scanning tools together, outputting results in a structured JSON format for easy analysis.

## Features

- **Subdomain Enumeration** - Discover subdomains using multiple passive and active sources
- **Port Scanning** - Fast port scanning to identify open services  
- **HTTP Fingerprinting** - Identify web technologies and server configurations
- **Automated OSINT Chaining** - Seamlessly chain reconnaissance tasks for comprehensive results
- **JSON Report Output** - Machine-readable output for easy integration with other tools

## Prerequisites

Install these required tools:

```bash
# Install Go (if not installed)
sudo apt install golang-go

# Install Subfinder (subdomain enumeration)
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Install httpx (HTTP probing)
go install github.com/projectdiscovery/httpx/cmd/httpx@latest

# Install nmap (port scanning)
sudo apt install nmap

# Add Go binaries to PATH
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc
```

## Installation

```bash
# Clone the repository
git clone https://github.com/Vuln-Z/recon-forge.git
cd recon-forge
```

## Usage

```bash
# Run recon on a target domain
python3 recon.py example.com

# Run with specific modules
python3 recon.py example.com --modules subdomains ports

# Specify output directory
python3 recon.py example.com -o my-results
```

## Options

- `domain` - Target domain (required)
- `-o, --output` - Output directory (default: results)
- `-m, --modules` - Modules to run: subdomains, ports, http

## Output

Results are saved in JSON format in the output directory.

## License

MIT License
