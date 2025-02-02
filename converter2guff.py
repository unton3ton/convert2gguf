# https://www.geeksforgeeks.org/how-to-convert-any-huggingface-model-to-gguf-file-format/

# Step 1: Download the Hugging Face Model

# pip install huggingface-hub

from huggingface_hub import login

login(token = "hf_Gplu*****tHizXlGKxoOG") # "hugging_face_access_token"

from huggingface_hub import snapshot_download

model_id = "mistralai/Mistral-Small-24B-Instruct-2501"  # Replace with the ID of the model you want to download
snapshot_download(repo_id=model_id, local_dir="mistral-small")



# Step 2: Set Up Llama.cpp
# Clone the Llama.cpp repository:

# git clone https://github.com/ggerganov/llama.cpp


# Navigate to the llama.cpp directory:

# cd llama.cpp


# Install the required dependencies:

# pip install -r requirements.txt



# Step 3: Convert the Model to GGUF Format
# Run the conversion script:

# python llama.cpp/convert-hf-to-gguf.py ./mistral-small --outfile mistral-small.gguf --outtype Q4_K_M 


# ./phi3: Path to the model directory.
# output_file.gguf: Name of the output file where the GGUF model will be saved.
# q8_0: Specifies the quantization type (in this case, quantized 8-bit integer).