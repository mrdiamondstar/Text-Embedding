Steps to follow and for understading of the code
# 1. SETUP
# Replace with your actual key if not using environment variables
# 2. THE DATA
# We have 3 sentences. Two are about animals, one is about finance.
# 3. GET VECTORS (The 1536 numbers)
# We ask OpenAI to turn text into numbers
# Extract the actual lists of numbers
# 4. DO THE MATH (Cosine Similarity)
# We compare Vector 1 (Cat) against the other two.
# Note: We wrap them in [ ] to make them 2D arrays, which the library expects.
# 5. PRINT RESULTS
# EXPECTED OUTPUT LOGIC
# Cat vs Kitten should be HIGH (e.g., 0.50 - 0.70)
# Cat vs Stocks should be LOW  (e.g., 0.10 - 0.20)