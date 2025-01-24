import torch
from transformers import pipeline

# Initialize the TinyLlama pipeline
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

def generate_response(user_message):
    """
    Generates a factual response using the TinyLlama model.
    """
    # Format the input message
    messages = [
        {
            "role": "system",
            "content": "You are a helpful and factual assistant that provides accurate and concise answers.",
        },
        {"role": "user", "content": user_message},
    ]
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    # Generate the response
    outputs = pipe(prompt, max_new_tokens=250, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    response = outputs[0]["generated_text"]
    
    # Extract only the assistant's response by removing the prompt
    assistant_response = response.split("<|assistant|>")[-1].strip()

    return assistant_response

