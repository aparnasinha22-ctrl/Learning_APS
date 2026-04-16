from langchain_openai import ChatOpenAI
import os
import httpx
client = httpx.Client(verify=False)
llm = ChatOpenAI(
base_url="https://genailab.tcs.in",
model = "azure_ai/genailab-maas-DeepSeek-V3-0324",
api_key="sk-vW_AOZkc3GwVOkzzn06KzQ",
http_client = client 
) 
response = llm.invoke("Hi") 
print(response)
