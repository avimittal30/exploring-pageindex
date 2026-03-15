"""
Clean PageIndex Demo
Shows what PageIndex excels at: complex queries on structured documents
"""

import os
import time
from pageindex import PageIndexClient
from dotenv import load_dotenv

load_dotenv()
client = PageIndexClient(api_key=os.getenv("pageindex_api_key"))


def get_sample_document():
    """Get path to sample PDF document"""
    filepath = "data/India_History.pdf"
    
    if not os.path.exists(filepath):
        print(f"❌ PDF not found at {filepath}")
        print("   Run: python convert_to_pdf.py")
        return None
    
    return filepath


def submit_document(filepath):
    """Submit document and wait for processing"""
    print(f"📤 Submitting: {filepath}")
    result = client.submit_document(filepath)
    doc_id = result["doc_id"]
    
    print(f"⏳ Processing...")
    while not client.is_retrieval_ready(doc_id):
        time.sleep(5)
    return doc_id


def show_tree(doc_id):
    """Display document tree structure"""
    print("="*80)
    print("DOCUMENT TREE STRUCTURE")
    print("="*80)
    import pageindex.utils as utils
    tree = client.get_tree(doc_id, node_summary=True)['result']
    utils.print_tree(tree)
    print()


def test_queries(doc_id):
    """Test queries PageIndex handles well"""
    queries = [
        "Compare the economy in Chalcolithic period and sangam period?",
        "what structural changes happened in the Iron age"
    ]
    
    print("="*80)
    print("TESTING QUERIES")
    print("="*80)
    
    for i, query in enumerate(queries, 1):
        print(f"\n[Query {i}] {query}")
        print("-"*80)
        
        # Use retrieval API
        response = client.submit_query(doc_id=doc_id, query=query)
        retrieval_id = response["retrieval_id"]
        
        # Wait for retrieval to complete
        max_retries = 30
        retry_count = 0
        retrieval = None
        
        while retry_count < max_retries:
            retrieval = client.get_retrieval(retrieval_id)
            status = retrieval.get("status")
            
            if status == "completed":
                break
            elif status == "failed":
                print(f"  ❌ Retrieval failed")
                break
            
            time.sleep(1)
            retry_count += 1
        
        if not retrieval or retrieval.get("status") != "completed":
            print(f"  ⚠️ Retrieval timeout or failed")
            continue
        
        nodes = retrieval.get("retrieved_nodes", [])
        print(f"Retrieved {len(nodes)} nodes")
        
        if nodes:
            for idx, node in enumerate(nodes[:3], 1):
                print(f"  {idx}. {node.get('node_title', 'Untitled')}")
            
            # Show first context
            for node in nodes[:1]:
                relevant_contents = node.get("relevant_contents", [])
                for group in relevant_contents[:1]:
                    for item in group[:1]:
                        content = item.get("relevant_content", "")
                        if content:
                            print(f"\nContext: {content}...")
                            break
        else:
            print("  ⚠️ No nodes retrieved")
        
        print()


def main():
    print("\nPageIndex Demo: Complex Query Handling\n")
    
    filepath = get_sample_document()
    if not filepath:
        return
    
    doc_id = submit_document(filepath)
    doc_id="pi-cmmr9kep3002iz7piqjr2iotm"
    show_tree(doc_id)
    test_queries(doc_id)
    
    print("="*80)
    print("KEY STRENGTHS")
    print("="*80)
    print("""
✅ Preserves document structure
✅ Handles multi-hop queries across sections
✅ Understands relationships and cross-references
✅ Explainable retrieval paths
    """)


if __name__ == "__main__":
    main()

