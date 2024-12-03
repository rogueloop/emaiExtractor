import argparse
from tools import mailcat, chiasmodon, msmailprobe, emailharvester

def run_tool(tool_name, domain):
    tools = {
        "mailcat": mailcat.run_mailcat,
        "chiasmodon": chiasmodon.run_chiasmodon,
        "msmailprobe": msmailprobe.run_msmailprobe,
        "emailharvester": emailharvester.run_emailharvester,
    }
    
    if tool_name in tools:
        return tools[tool_name](domain)
    else:
        raise ValueError(f"Tool {tool_name} is not supported.")

def main():
    parser = argparse.ArgumentParser(description="Unified OSINT Toolkit for Email Enumeration")
    parser.add_argument("--tool", type=str, help="Tool to run (e.g., mailcat, chiasmodon)")
    parser.add_argument("--domain", type=str, required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("--run-all", action="store_true", help="Run all tools")
    args = parser.parse_args()

    if args.run_all:
        print("Running all tools...")
        results = [run_tool(tool, args.domain) for tool in ["mailcat", "chiasmodon", "msmailprobe", "emailharvester"]]
        print("Aggregated Results:", results)
    else:
        if not args.tool:
            print("Please specify a tool or use --run-all to execute all tools.")
        else:
            result = run_tool(args.tool, args.domain)
            print(f"Results from {args.tool}:", result)

if __name__ == "__main__":
    main()
