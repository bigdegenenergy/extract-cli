#!/usr/bin/env python3
"""
CLI Template for extract-cli Framework

This template provides a starting point for creating an interactive CLI
that guides users through describing their task and seeing cost estimates.
"""

import os
import sys
from typing import Optional


def print_header(framework_name: str):
    """Print CLI header."""
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║                  {framework_name:^48s}                  ║
║                   Interactive CLI                             ║
╚═══════════════════════════════════════════════════════════════╝
""")


def get_api_key(env_var_name: str = 'OPENROUTER_API_KEY') -> Optional[str]:
    """Get API key from user or environment."""
    api_key = os.getenv(env_var_name)
    
    if not api_key:
        print(f"\n⚠️  {env_var_name} not found in environment.")
        print("You can get a free API key at: https://openrouter.ai/")
        print("\nOptions:")
        print(f"1. Set environment variable: export {env_var_name}='your-key'")
        print("2. Enter it now (not recommended for security)")
        
        choice = input("\nEnter API key now? (y/n): ").strip().lower()
        if choice == 'y':
            api_key = input("API Key: ").strip()
        else:
            print("\n❌ Cannot proceed without API key. Exiting.")
            return None
    
    return api_key


def get_task_input() -> tuple:
    """Get task description from user."""
    print("\n" + "="*70)
    print("STEP 1: Describe Your Task")
    print("="*70)
    
    print("\nWhat task would you like to accomplish?")
    print("(Be as specific as possible about what needs to be done)")
    print("\nExamples:")
    print("  - 'Solve the 15-disk Towers of Hanoi puzzle'")
    print("  - 'Generate a 10-chapter novel outline'")
    print("  - 'Plan a 30-day marketing campaign'\n")
    
    task_description = input("Task: ").strip()
    
    if not task_description:
        print("❌ Task description cannot be empty.")
        return None, None
    
    print("\nWhat defines success for this task?")
    print("(Optional - press Enter to use default)\n")
    
    success_criteria = input("Success criteria: ").strip()
    if not success_criteria:
        success_criteria = "Task completed successfully with all requirements met"
    
    return task_description, success_criteria


def confirm_analysis(analysis: dict) -> bool:
    """Show analysis and get user confirmation."""
    print("\n" + "="*70)
    print("STEP 2: Task Analysis")
    print("="*70)
    
    print(f"\n📊 Estimated Steps: {analysis.get('estimated_steps', 'Unknown'):,}")
    
    print("\n" + "-"*70)
    choice = input("\nDoes this analysis look correct? (y/n): ").strip().lower()
    return choice == 'y'


def show_cost_estimate(estimate: dict) -> bool:
    """Show cost estimate and get user confirmation."""
    print("\n" + "="*70)
    print("STEP 3: Cost Estimation")
    print("="*70)
    
    print(f"\nModel: {estimate.get('model', 'Unknown')}")
    print(f"Estimated Calls: {estimate.get('estimated_calls', 0):,}")
    print(f"Estimated Cost: ${estimate.get('total_cost', 0):.4f}")
    
    if estimate.get('total_cost', 0) < 0.01:
        print("\n💰 This task will cost less than $0.01 to run!")
    elif estimate.get('total_cost', 0) < 0.10:
        print("\n💰 This is a very affordable task to run.")
    else:
        print("\n💵 This task has a reasonable cost.")
    
    print("\n" + "-"*70)
    choice = input("\nProceed with execution? (y/n): ").strip().lower()
    return choice == 'y'


def main():
    """Main CLI entry point."""
    print_header("Your Framework Name")
    
    # Get API key
    api_key = get_api_key()
    if not api_key:
        return 1
    
    # Get task input
    task_description, success_criteria = get_task_input()
    if not task_description:
        return 1
    
    print("\n🔄 Analyzing task...")
    
    # TODO: Implement task analysis
    # analysis = analyze_task(task_description, success_criteria)
    
    # TODO: Show analysis and get confirmation
    # if not confirm_analysis(analysis):
    #     print("\n❌ Task analysis rejected. Exiting.")
    #     return 1
    
    # TODO: Estimate cost
    # cost_estimate = estimate_cost(analysis)
    
    # TODO: Show cost and get confirmation
    # if not show_cost_estimate(cost_estimate):
    #     print("\n❌ Execution cancelled by user.")
    #     return 0
    
    print("\n✅ Configuration saved!")
    print("\nNext steps:")
    print("  1. Review the generated configuration")
    print("  2. Run the execution script")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
