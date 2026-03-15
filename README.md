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


