# ReconForge - Automated Bug Bounty Recon Tool

ReconForge is an automated reconnaissance framework designed for bug bounty hunters and security researchers. It streamlines the initial information gathering phase by chaining multiple OSINT and network scanning tools together, outputting results in a structured JSON format for easy analysis.

## Features

- **Subdomain Enumeration** - Discover subdomains using multiple passive and active sources
- **Port Scanning** - Fast port scanning to identify open services
- **HTTP Fingerprinting** - Identify web technologies and server configurations
- **Automated OSINT Chaining** - Seamlessly chain reconnaissance tasks for comprehensive results
- **JSON Report Output** - Machine-readable output for easy integration with other tools

## Installation

```bash
# Clone the repository
git clone https://github.com/Vuln-Z/recon-forge.git
cd recon-forge

# install -r requirements.txt
```

## Usage

 Install dependencies
pip```bash
python reconforge.py -t example.com
```

## License

MIT License - see LICENSE file for details
