# PageIndex Demo

A practical demonstration of PageIndex's hierarchical document understanding and automatic section summarization.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file:

```bash
pageindex_api_key=your_api_key_here
```

Get your API key from: https://dash.pageindex.ai/

### 3. Run the Demo

```bash
python clean_demo.py
```

## 🔍 Key Features

- **Automatic hierarchical tree extraction** from PDFs
- **AI-generated section summaries** at every level
- **Structure-aware querying** for complex questions
- **Direct navigation** via tree indexing

## 📖 Accessing Document Structure

```python
# Get document tree with summaries
tree = client.get_tree(doc_id, node_summary=True)['result']

# Access section summary
section_summary = tree[0]['nodes'][2]['summary']

# Access subsection summary
subsection_summary = tree[0]['nodes'][2]['nodes'][8]['summary']
```

## 📚 Learn More

**Complete guide with honest evaluation**: [PageIndex_Guide.md](PageIndex_Guide.md)

Covers: when to use PageIndex, latency considerations, vector DB comparisons, cost analysis, and tradeoffs.

## 📄 Resources

- **Documentation**: https://docs.pageindex.ai/
- **API Key**: https://dash.pageindex.ai/
- Part 3: How PageIndex handles these queries
- Part 4: Side-by-side comparison table

**Time:** 2-3 minutes

### Demo 2: Live PageIndex API

See actual tree-based retrieval in action:

```bash
# 1. Get free API key
# Visit: https://dash.pageindex.ai/
# Sign up and generate API key

# 2. Create .env file
echo "pageindex_api_key=your_key_here" > .env

# 3. Run demo
python pageindex_demo.py
```

**What you'll see:**
- Document submission and tree generation
- Full hierarchical tree structure printed
- 4 complex queries with reasoning paths
- Retrieved context with structural information
- Chat API demonstration

**Time:** 5-10 minutes (includes document processing)

### Demo 3: Traditional Vector RAG (Optional)

Compare with traditional approach:

```bash
# 1. Install additional dependencies
pip install langchain chromadb pypdf openai tiktoken

# 2. Add OpenAI key to .env
echo "OPENAI_API_KEY=your_key" >> .env

# 3. Run demo
python vector_rag_demo.py
```

**What you'll see:**
- PDF loading and chunking
- Vector database creation
- Query attempts showing limitations
- Clear explanation of each failure

## The Test Document

We use a synthetic company annual report (`synthetic_document.py`) that includes:

- **Length:** ~17,000 characters
- **Structure:** 7 major sections, 20+ subsections
- **Content:** Realistic business data with:
  - Financial metrics across multiple sections
  - Cross-references (e.g., "As mentioned in Section 3.1...")
  - Hierarchical breakdowns (total → segments → products)
  - Comparative data (2024 vs 2025)
  - Dependencies (risks → financial impacts)

This structure is *intentional* - it mimics real documents where relationships matter.

## Example Queries That Demonstrate the Difference

### Query 1: Multi-Hop Reasoning
```
"How does the R&D investment in the reasoning engine relate to 
the company's path to profitability and competitive advantages?"
```

**Vector RAG:** Returns separate chunks about R&D, profitability, and competition. No understanding of relationships.

**PageIndex:** Navigates to Section 3.1.1 (R&D), Section 2.2 (profitability), Section 6.1 (competition), notices cross-reference in Section 6.5, synthesizes with relationships intact.

### Query 2: Aggregation
```
"What are all the different revenue figures mentioned across 
the document and how do they relate to each other?"
```

**Vector RAG:** Retrieves chunks mentioning "revenue" but cannot systematically aggregate or show hierarchical relationships.

**PageIndex:** Traverses tree to find all revenue mentions, understands $500M total breaks down into products ($320M + $120M + $60M) and segments ($430M + $50M + $20M).

### Query 3: Dependency Tracking
```
"Which risks mentioned in the risk section directly impact 
the financial metrics discussed earlier?"
```

**Vector RAG:** Returns risk chunks and financial chunks separately. No causal understanding.

**PageIndex:** Navigates to Section 6 (risks), connects LLM costs (6.2) → gross margin (2.2), scaling (6.4) → cash burn (2.3), understands impact relationships.

## Understanding the Output

### PageIndex Reasoning Path

When you run the PageIndex demo, you'll see output like:

```
🧠 REASONING PATH (How PageIndex navigated the tree):
─────────────────────────────────────────────────────────────
1. Visited Node: Section 3.1.1 - Reasoning Engine
   Path: Root → R&D → AI Model Development → Reasoning Engine
   Relevance Score: 0.94

2. Visited Node: Section 2.2 - Profitability Metrics  
   Path: Root → Financial Performance → Profitability
   Relevance Score: 0.89

3. Visited Node: Section 6.1 - Competitive Risks
   Path: Root → Risk Factors → Competitive Risks
   Relevance Score: 0.87
```

This shows:
- ✅ Which nodes were explored
- ✅ The hierarchical path to each node
- ✅ Why each node was considered relevant
- ✅ Complete traceability and explainability

### Vector RAG Output

Traditional RAG shows:

```
[Chunk 37] Similarity Score: 0.82
"...R&D investment $35M focusing on reasoning engine development..."

[Chunk 51] Similarity Score: 0.79  
"...operating margin -15%, path to profitability Q2 2026..."

[Chunk 64] Similarity Score: 0.76
"...competitive advantages include proprietary technology..."
```

**Problem:** These chunks are retrieved independently. The system doesn't know they're related or how they connect.

## When to Use Each Approach

### Use PageIndex When:

✅ Documents have hierarchical structure (reports, contracts, papers)  
✅ Queries require multi-hop reasoning  
✅ Cross-references are important  
✅ You need explainable retrieval  
✅ Aggregation across sections is needed  

### Use Vector RAG When:

✅ Simple similarity matching is sufficient  
✅ Documents are unstructured (chats, posts)  
✅ Scale is more important than precision  
✅ You need very fast retrieval  
✅ Documents are short and independent  

### Use Both (Hybrid):

Many production systems route queries based on complexity and document type.

## Cost Comparison

### Vector RAG Costs:
- Embedding API calls: $0.0001 per 1K tokens (OpenAI Ada-002)
- Vector DB hosting: ~$50-200/month (Pinecone, Weaviate)
- Low per-query cost

### PageIndex Costs (Free Tier):
- 200 free tree generation pages
- 100 free chat API queries
- No vector DB hosting needed
- Paid plans: $0.01/page for tree generation, $0.02/query for chat

## Read the Full Article

See [ARTICLE.md](ARTICLE.md) for a comprehensive explanation including:
- Detailed problem analysis
- Visual examples of chunking failures
- Step-by-step PageIndex workflow
- Trade-offs and limitations
- Production considerations

## Troubleshooting

### "Module not found: pageindex"
```bash
pip install pageindex
```

### "API key not found"
Create a `.env` file:
```
pageindex_api_key=your_key_here
```

Get free key at: https://dash.pageindex.ai/

### "Document processing timeout"
Processing can take 1-2 minutes for PDFs. The demo waits up to 10 minutes. If it times out, check your API quota.

### Want to test with your own documents?

Modify `pageindex_demo.py`:
```python
# Replace this line:
pdf_path = download_research_paper(pdf_url, "2501.12948.pdf")

# With:
pdf_path = "path/to/your/document.pdf"
```

## Resources

- **PageIndex Documentation:** https://docs.pageindex.ai/
- **Get Free API Key:** https://dash.pageindex.ai/
- **PageIndex GitHub:** https://github.com/VectifyAI/PageIndex
- **Discord Community:** https://discord.gg/VuXuf29EUj

## Contributing

Found an issue or have suggestions? This demo is meant to be educational. Contributions welcome:

- Improve synthetic documents
- Add more test queries
- Create domain-specific examples (legal, medical, technical)
- Compare with other retrieval methods

## License

This demo code is provided for educational purposes. The PageIndex API requires an account and follows their terms of service.

---

**Start here:** Run `python comparison_demo.py` to see the differences in action!
