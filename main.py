import streamlit as st
import requests

API_BASE_URL = "http://0.0.0.0:4658"  # Adjust the base URL as needed

def call_api(endpoint, method='GET', data=None, params=None, files=None):
    url = f"{API_BASE_URL}{endpoint}"
    try:
        if method == 'GET':
            response = requests.get(url, params=params)
        elif method == 'POST':
            response = requests.post(url, json=data, params=params, files=files)
        elif method == 'PUT':
            response = requests.put(url, json=data, params=params)
        elif method == 'DELETE':
            response = requests.delete(url, json=data, params=params)
        elif method == 'PATCH':
            response = requests.patch(url, json=data, params=params)

        response.raise_for_status()
        try:
            json_response = response.json()
            if isinstance(json_response, dict) or isinstance(json_response, list):
                return json_response
            else:
                st.error("Invalid JSON response")
                return None
        except ValueError:
            st.error("Failed to parse JSON response")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"API call failed: {e}")
        return None

def display_api_response(endpoint, method='GET', data=None):
    if st.button(f"Call {method} {endpoint}"):
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_signup_user_api():
    user_name = st.text_input("User Name", key="signup_user_name")
    user_email = st.text_input("User Email", key="signup_user_email")
    password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Sign Up User"):
        endpoint = "/signup_user"
        method = 'POST'
        data = {
            "user_name": user_name,
            "user_email": user_email,
            "password": password
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_login_user_api():
    user_email = st.text_input("User Email", key="login_user_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login User"):
        endpoint = "/login_user"
        method = 'POST'
        data = {
            "user_email": user_email,
            "password": password
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_new_chatbot_api():
    user_id = st.text_input("User ID", key="new_chatbot_user_id")
    chatbot_name = st.text_input("Chatbot Name", key="new_chatbot_name")
    chatbot_desc = st.text_input("Chatbot Description", key="new_chatbot_desc")
    chatbot_image_path = st.text_input("Chatbot Image Path", key="new_chatbot_image_path")
    if st.button("Create New Chatbot"):
        endpoint = "/new_chatbot"
        method = 'POST'
        data = {
            "user_id": user_id,
            "chatbot_name": chatbot_name,
            "chatbot_desc": chatbot_desc,
            "chatbot_image_path": chatbot_image_path
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_show_chatbot_api():
    user_id = st.text_input("User ID", key="show_chatbot_user_id")
    if st.button("Show Chatbots"):
        endpoint = "/show_chatbot"
        method = 'GET'
        params = {"user_id": user_id}
        response = call_api(endpoint, method, params=params)
        if response is not None:
            st.json(response)

def call_delete_chatbot_api():
    user_id = st.text_input("User ID", key="delete_chatbot_user_id")
    chatbot_id = st.text_input("Chatbot ID", key="delete_chatbot_id")
    if st.button("Delete Chatbot"):
        endpoint = "/delete_chatbot"
        method = 'DELETE'
        data = {
            "user_id": user_id,
            "chatbot_id": chatbot_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_show_config_api():
    chatbot_id = st.text_input("Chatbot ID", key="show_config_chatbot_id")
    if st.button("Show Config"):
        endpoint = "/show_config"
        method = 'GET'
        params = {"chatbot_id": chatbot_id}
        response = call_api(endpoint, method, params=params)
        if response is not None:
            st.json(response)

def call_save_config_api():
    chatbot_id = st.text_input("Chatbot ID", key="save_config_chatbot_id")
    config_data = {
        "chatbot_name": st.text_input("Chatbot Name", key="save_config_chatbot_name"),
        "chatbot_desc": st.text_input("Chatbot Description", key="save_config_chatbot_desc"),
        "ai_engine": st.text_input("AI Engine", key="save_config_ai_engine"),
        "temperature": st.number_input("Temperature", value=0.7, key="save_config_temperature"),
        "max_response": st.number_input("Max Response", value=150, key="save_config_max_response"),
        "sys_prompt": st.text_input("System Prompt", key="save_config_sys_prompt"),
        "num_prompt_tokens": st.number_input("Number of Prompt Tokens", value=50, key="save_config_num_prompt_tokens"),
        "rerank_model": st.text_input("Rerank Model", key="save_config_rerank_model"),
        "knowledge_relevance": st.number_input("Knowledge Relevance", value=0.8, key="save_config_knowledge_relevance"),
        "recall_num": st.number_input("Recall Number", value=5, key="save_config_recall_num"),
        "search_weight": st.number_input("Search Weight", value=0.5, key="save_config_search_weight"),
        "mixed_percentage": st.number_input("Mixed Percentage", value=0.3, key="save_config_mixed_percentage"),
        "empty_response": st.text_input("Empty Response", key="save_config_empty_response"),
        "memory": st.number_input("Memory", value=5, key="save_config_memory")
    }
    if st.button("Save Config"):
        endpoint = "/save_config"
        method = 'POST'
        data = {
            "chatbot_id": chatbot_id,
            **config_data
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_create_knowledge_base_api():
    chatbot_id = st.text_input("Chatbot ID", key="create_knowledge_base_chatbot_id")
    knowledge_name = st.text_input("Knowledge Base Name", key="create_knowledge_base_name")
    knowledge_desc = st.text_input("Knowledge Base Description", key="create_knowledge_base_desc")
    if st.button("Create Knowledge Base"):
        endpoint = f"/api/knowledge-base/create/{chatbot_id}"
        method = 'POST'
        data = {
            "knowledge_name": knowledge_name,
            "knowledge_desc": knowledge_desc
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_get_knowledge_base_config_api():
    chatbot_id = st.text_input("Chatbot ID", key="get_knowledge_base_config_chatbot_id")
    knowledge_id = st.text_input("Knowledge Base ID", key="get_knowledge_base_config_id")
    if st.button("Get Knowledge Base Config"):
        endpoint = f"/api/knowledge-base/get-config/{knowledge_id}"
        method = 'GET'
        params = {"chatbot_id": chatbot_id}
        response = call_api(endpoint, method, params=params)
        if response is not None:
            st.json(response)

def call_configure_knowledge_base_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="configure_knowledge_base_id")
    chatbot_id = st.text_input("Chatbot ID", key="configure_knowledge_base_chatbot_id")
    config_data = {
        "knowledge_name": st.text_input("Knowledge Base Name", key="configure_knowledge_base_name"),
        "knowledge_desc": st.text_input("Knowledge Base Description", key="configure_knowledge_base_desc")
    }
    if st.button("Configure Knowledge Base"):
        endpoint = f"/api/knowledge-base/configure/{knowledge_id}"
        method = 'POST'
        data = {
            "chatbot_id": chatbot_id,
            **config_data
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_list_knowledge_bases_api():
    chatbot_id = st.text_input("Chatbot ID", key="list_knowledge_bases_chatbot_id")
    if st.button("List Knowledge Bases"):
        endpoint = f"/api/knowledge-base/show/{chatbot_id}"
        method = 'GET'
        response = call_api(endpoint, method)
        if response is not None:
            st.json(response)

def call_get_knowledge_base_status_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="get_knowledge_base_status_id")
    if st.button("Get Knowledge Base Status"):
        endpoint = f"/api/knowledge-base/status/{knowledge_id}"
        method = 'GET'
        response = call_api(endpoint, method)
        if response is not None:
            st.json(response)

def call_upload_to_knowledge_base_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="upload_to_knowledge_base_id")
    chatbot_id = st.text_input("Chatbot ID", key="upload_to_knowledge_base_chatbot_id")
    files = st.file_uploader("Upload Files", accept_multiple_files=True, key="upload_to_knowledge_base_files")
    if st.button("Upload to Knowledge Base"):
        endpoint = f"/api/knowledge-base/upload/{knowledge_id}"
        method = 'POST'
        files_data = [("files", file) for file in files]
        data = {
            "chatbot_id": chatbot_id
        }
        response = call_api(endpoint, method, data=data, files=files_data)
        if response is not None:
            st.json(response)

def call_list_knowledge_base_documents_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="list_knowledge_base_documents_id")
    if st.button("List Knowledge Base Documents"):
        endpoint = f"/api/knowledge-base/list/{knowledge_id}"
        method = 'GET'
        response = call_api(endpoint, method)
        if response is not None:
            st.json(response)

def call_get_usage_metrics_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="get_usage_metrics_id")
    if st.button("Get Usage Metrics"):
        endpoint = f"/api/knowledge-base/usage-metrics/{knowledge_id}"
        method = 'GET'
        response = call_api(endpoint, method)
        if response is not None:
            st.json(response)

def call_update_retrieval_status_api():
    doc_id = st.text_input("Document ID", key="update_retrieval_status_doc_id")
    enable_retrieval = st.checkbox("Enable Retrieval", key="update_retrieval_status_enable_retrieval")
    if st.button("Update Retrieval Status"):
        endpoint = f"/api/knowledge-base/update/{doc_id}"
        method = 'PATCH'
        params = {
            "enable_retrieval": enable_retrieval
        }
        response = call_api(endpoint, method, params=params)
        if response is not None:
            st.json(response)

def call_remove_from_knowledge_base_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="remove_from_knowledge_base_id")
    doc_id = st.text_input("Document ID", key="remove_from_knowledge_base_doc_id")
    if st.button("Remove Document from Knowledge Base"):
        endpoint = f"/api/knowledge-base/remove/{knowledge_id}/{doc_id}"
        method = 'DELETE'
        response = call_api(endpoint, method)
        if response is not None:
            st.json(response)

def call_remove_knowledge_base_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="remove_knowledge_base_id")
    chatbot_id = st.text_input("Chatbot ID", key="remove_knowledge_base_chatbot_id")
    if st.button("Remove Knowledge Base"):
        endpoint = f"/api/knowledge-base/remove/{knowledge_id}"
        method = 'DELETE'
        data = {
            "chatbot_id": chatbot_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_vector_search_submit_api():
    knowledge_id = st.text_input("Knowledge Base ID", key="vector_search_submit_id")
    query = st.text_input("Query", key="vector_search_submit_query")
    top_k = st.number_input("Top K", value=5, key="vector_search_submit_top_k")
    if st.button("Submit Vector Search"):
        endpoint = f"/vector-search/submit/{knowledge_id}"
        method = 'POST'
        data = {
            "query": query,
            "top_k": top_k
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_query_api():
    query = st.text_input("Query", key="query_api_query")
    knowledge_id = st.text_input("Knowledge Base ID", key="query_api_knowledge_id")
    dialog_id = st.text_input("Dialog ID", key="query_api_dialog_id")
    if st.button("Submit Query"):
        endpoint = "/query/submit"
        method = 'POST'
        data = {
            "query": query,
            "knowledge_id": knowledge_id,
            "dialog_id": dialog_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_new_dialog_api():
    user_id = st.text_input("User ID", key="new_dialog_user_id")
    chatbot_id = st.text_input("Chatbot ID", key="new_dialog_chatbot_id")
    if st.button("New Dialog"):
        endpoint = "/dialog/new_dialog"
        method = 'POST'
        data = {
            "user_id": user_id,
            "chatbot_id": chatbot_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_select_dialog_api():
    user_id = st.text_input("User ID", key="select_dialog_user_id")
    chatbot_id = st.text_input("Chatbot ID", key="select_dialog_chatbot_id")
    dialog_id = st.text_input("Dialog ID", key="select_dialog_dialog_id")
    if st.button("Select Dialog"):
        endpoint = "/dialog/select_dialog"
        method = 'POST'
        data = {
            "user_id": user_id,
            "chatbot_id": chatbot_id,
            "dialog_id": dialog_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_deselect_dialog_api():
    user_id = st.text_input("User ID", key="deselect_dialog_user_id")
    chatbot_id = st.text_input("Chatbot ID", key="deselect_dialog_chatbot_id")
    dialog_id = st.text_input("Dialog ID", key="deselect_dialog_dialog_id")
    if st.button("Deselect Dialog"):
        endpoint = "/dialog/deselect_dialog"
        method = 'POST'
        data = {
            "user_id": user_id,
            "chatbot_id": chatbot_id,
            "dialog_id": dialog_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_show_dialog_api():
    user_id = st.text_input("User ID", key="show_dialog_user_id")
    chatbot_id = st.text_input("Chatbot ID", key="show_dialog_chatbot_id")
    if st.button("Show Dialogs"):
        endpoint = "/dialog/show_dialog"
        method = 'GET'
        params = {
            "user_id": user_id,
            "chatbot_id": chatbot_id
        }
        response = call_api(endpoint, method, params=params)
        if response is not None:
            st.json(response)

def call_delete_dialog_api():
    user_id = st.text_input("User ID", key="delete_dialog_user_id")
    chatbot_id = st.text_input("Chatbot ID", key="delete_dialog_chatbot_id")
    dialog_id = st.text_input("Dialog ID", key="delete_dialog_dialog_id")
    if st.button("Delete Dialog"):
        endpoint = "/dialog/delete_dialog"
        method = 'DELETE'
        data = {
            "user_id": user_id,
            "chatbot_id": chatbot_id,
            "dialog_id": dialog_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def call_show_conversation_api():
    dialog_id = st.text_input("Dialog ID", key="show_conversation_dialog_id")
    if st.button("Show Conversation"):
        endpoint = "/query/retrieve"
        method = 'GET'
        params = {"dialog_id": dialog_id}
        response = call_api(endpoint, method, params=params)
        if response is not None:
            st.json(response)

def call_clear_conversation_api():
    dialog_id = st.text_input("Dialog ID", key="clear_conversation_dialog_id")
    if st.button("Clear Conversation"):
        endpoint = "/query/reset-history"
        method = 'DELETE'
        data = {
            "dialog_id": dialog_id
        }
        response = call_api(endpoint, method, data)
        if response is not None:
            st.json(response)

def main():
    st.title("API User Acceptance Testing (UAT) Interface")

    section = st.sidebar.selectbox("Select Section", ["User Endpoints", "Chatbot Endpoints", "Knowledge Base Endpoints", "Vector Search Endpoints", "Dialog Endpoints", "Conversation Endpoints"])

    if section == "User Endpoints":
        with st.expander("User Endpoints"):
            call_signup_user_api()
            call_login_user_api()

    if section == "Chatbot Endpoints":
        with st.expander("Chatbot Endpoints"):
            call_new_chatbot_api()
            call_show_chatbot_api()
            call_delete_chatbot_api()
            call_show_config_api()
            call_save_config_api()

    if section == "Knowledge Base Endpoints":
        with st.expander("Knowledge Base Endpoints"):
            call_create_knowledge_base_api()
            call_get_knowledge_base_config_api()
            call_configure_knowledge_base_api()
            call_list_knowledge_bases_api()
            call_get_knowledge_base_status_api()
            call_upload_to_knowledge_base_api()
            call_list_knowledge_base_documents_api()
            call_get_usage_metrics_api()
            call_update_retrieval_status_api()
            call_remove_from_knowledge_base_api()
            call_remove_knowledge_base_api()

    if section == "Vector Search Endpoints":
        with st.expander("Vector Search Endpoints"):
            call_vector_search_submit_api()
            call_query_api()

    if section == "Dialog Endpoints":
        with st.expander("Dialog Endpoints"):
            call_new_dialog_api()
            call_select_dialog_api()
            call_deselect_dialog_api()
            call_show_dialog_api()
            call_delete_dialog_api()

    if section == "Conversation Endpoints":
        with st.expander("Conversation Endpoints"):
            call_show_conversation_api()
            call_clear_conversation_api()

if __name__ == "__main__":
    main()
