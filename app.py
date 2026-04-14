import gradio as gr
from BasicAgent import agent, is_injection, llm, SYSTEM_PROMPT

def chat(message, history):
    blocked, reason = is_injection(message, llm)
    if blocked:
        return f"⚠️ Query blocked: {reason}."

    result = agent.invoke({"messages": [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message},
    ]})
    return result["messages"][-1].content

with gr.Blocks() as demo:
    gr.Markdown("## SafeRAG Assistant")
    gr.Markdown("Ask questions from your documents or search the web. Harmful and injection attempts are blocked.")

    chatbot = gr.Chatbot()
    textbox = gr.Textbox(placeholder="Ask something...", show_label=False)

    with gr.Row():
        submit = gr.Button("Send", variant="primary")
        clear = gr.Button("Clear History", variant="secondary")

    gr.ChatInterface(
        fn=chat,
        chatbot=chatbot,
        textbox=textbox,
        submit_btn=False,
    )

    submit.click(fn=chat, inputs=[textbox, chatbot], outputs=[chatbot])
    clear.click(fn=lambda: [], outputs=[chatbot])

demo.launch()
