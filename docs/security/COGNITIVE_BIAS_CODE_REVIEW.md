# Mitigating Cognitive Bias & Blind Spots in DevSecOps Peer Reviews

## Executive Summary
Human code review is an essential layer in supply chain defense. Adversaries exploit cognitive fatigue and confirmation bias to sneak backdoor commits into large pull requests.

## Counter-Bias Controls
1. **Diff Size Thresholds**: Pull requests exceeding 500 lines of application logic require dual-reviewer sign-off.
2. **Context Blind Reviewing**: Code reviewers verify logic without viewing author seniority badges.
3. **Structured Review Checklists**: Focus specifically on:
   - Dynamic reflection or dynamic module imports
   - Deserialization routines (`pickle`, `yaml.load`)
   - Direct subprocess execution
   - Cryptographic constant-time comparisons
