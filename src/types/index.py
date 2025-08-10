# This file defines any custom types or data structures used throughout the project, ensuring type safety and clarity in function signatures.

from typing import List, Dict, Any

# Define a type for the skill matrix
SkillMatrix = Dict[str, List[int]]

# Define a type for job postings
JobPosting = Dict[str, Any]

# Define a type for clustering results
ClusteringResult = Dict[str, Any]