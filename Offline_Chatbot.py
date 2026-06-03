from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')
qa_pairs = [
    ("hello hi hey greetings", "Hi! How can I help with technology today?"),
    ("computer pc hardware cpu gpu motherboard ram",
     "Do you want help building or upgrading your PC? I can suggest parts."),
    ("phone smartphone android iphone ios", "Need help choosing a phone or fixing an issue on Android/iPhone?"),
    ("laptop notebook ultrabook macbook", "Tell me your budget and use, and I’ll suggest a good laptop."),
    ("tablet ipad android tablet", "Tablets are great for media and light work—need a recommendation?"),
    ("internet wifi connection slow lag", "Try restarting your router, moving closer, or changing the WiFi channel."),
    ("router modem setup network", "I can guide you step-by-step to set up your router or fix network issues."),
    ("programming coding python java c++ javascript", "Learning to code? I can help with concepts, bugs, or projects."),
    ("bug error crash issue problem", "Share the error message or what happens, and I’ll help debug it."),
    ("software app application install uninstall", "Need help installing, removing, or choosing software?"),
    ("windows microsoft os", "Are you having an issue with Windows or need optimization tips?"),
    ("mac macos apple", "I can help with macOS shortcuts, fixes, or performance tips."),
    ("linux ubuntu debian terminal", "Linux is powerful! Need help with commands or setup?"),
    ("security virus malware hacker antivirus", "Run a full scan, update your system, and avoid unknown downloads."),
    ("privacy data tracking cookies", "Use privacy-focused browsers, VPNs, and limit app permissions."),
    ("vpn proxy anonymity", "VPNs help protect privacy—want recommendations or setup help?"),
    ("cloud storage drive dropbox icloud", "Cloud storage is great foar backups and syncing across devices."),
    ("backup data external hard drive", "Always keep backups—cloud + external drive is safest."),
    ("gaming pc console playstation xbox fps lag", "Want better FPS or game recommendations? Tell me your setup."),
    ("graphics gpu drivers nvidia amd", "Updating GPU drivers can fix performance and compatibility issues."),
    (
    "ai artificial intelligence machine learning chatgpt", "Want to learn AI basics or how to use tools like ChatGPT?"),
    ("website web development html css javascript frontend backend", "I can help you build websites or learn web dev."),
    ("database sql mysql postgres", "Need help with databases, queries, or design?"),
    ("api rest graphql", "APIs connect apps—want help building or using one?"),
    ("mobile app development android ios flutter react native", "Interested in building apps? I can guide you."),
    ("battery charging phone laptop", "Avoid overcharging and extreme heat to extend battery life."),
    ("performance slow computer lagging", "Try cleaning startup apps, freeing space, or upgrading RAM."),
    ("storage ssd hdd nvme", "SSDs are much faster than HDDs—great upgrade for performance."),
    ("monitor display resolution refresh rate", "Higher refresh rates (144Hz+) are great for gaming."),
    ("keyboard mouse peripherals", "Mechanical keyboards and good mice improve productivity and gaming."),
    ("bluetooth pairing connection issue", "Turn Bluetooth off/on and re-pair the device."),
    ("email gmail outlook problem", "Check spam, filters, and server settings."),
    ("password reset account login", "Use password managers and enable 2FA for security."),
    ("two factor authentication 2fa security", "2FA adds an extra layer of protection to your accounts."),
    ("update upgrade software firmware", "Keeping software updated improves security and performance."),
    ("smart home iot alexa google home", "Smart devices can automate your home—need setup help?"),
    ("streaming netflix youtube buffering", "Buffering issues? Check internet speed and reduce background usage."),
    ("file format convert pdf jpg png mp4", "I can help you convert files or choose the right format."),
    ("printer printing problem ink", "Check drivers, ink levels, and connection settings."),
    ("usb device not recognized", "Try another port, cable, or reinstall drivers."),
    ("heat overheating cpu laptop", "Clean dust and ensure proper airflow to avoid overheating."),
    ("cooling fan noise loud", "Loud fans may mean dust buildup or high CPU usage."),
    ("build pc guide custom pc", "I can guide you step-by-step to build your own PC."),
    ("budget cheap tech recommendations", "Tell me your budget and I’ll suggest the best value options."),
    ("future technology trends ai vr ar", "AI, VR, and AR are shaping the future—want an overview?"),
    ("thanks thank you appreciate", "You're welcome! Let me know if you have more tech questions."),
    ("browser chrome firefox edge safari", "Which browser are you using? I can help with speed, extensions, or issues."),
    ("extensions plugins addons", "Browser extensions can boost productivity—want some recommendations?"),
    ("video editing software premiere davinci", "Need help choosing or learning video editing tools?"),
    ("audio music editing audacity daw", "I can suggest tools and tips for recording or editing audio."),
    ("online meeting zoom teams skype",
     "Having issues with calls? I can help fix audio, video, or connection problems."),
]
# Pre-compute embeddings for all question patterns
question_texts = [q for q, a in qa_pairs]
question_embeddings = model.encode(question_texts, convert_to_tensor=True)

# Similarity threshold — below this, the bot says it doesn't understand
THRESHOLD = 0.3


# Semantic matching replaces keyword matching
def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)

    similarities = util.cos_sim(input_embedding, question_embeddings)[0]

    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()

    if best_score < THRESHOLD:
        return (
            best_score,
            "Sorry, I don't understand. Try asking about PC, Programming, or AI!"
        )

    return best_score, qa_pairs[best_idx][1]
class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Technology Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#2E2E2E")

        # Title
        tk.Label(
            root, text="Technology Chatbot", font=("Helvetica", 16, "bold"),
            fg="#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        # Chat area (scrollable)
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=20, width=50, font=("Arial", 11),
            bg="#3C3C3C", fg="#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "Welcome to the Technology Chatbot!\n"
                              "Ask me anything about technology (e.g., 'my WiFi is slow', 'recommend a laptop', or 'programming help').\n")
        self.chat_area.config(state='disabled')

        input_frame = tk.Frame(root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        # Input field
        self.input_field = tk.Entry(
            input_frame,
            width=40,
            font=("Arial", 11),
            bg="#4A4A4A",
            fg="#FFFFFF",
            insertbackground="white"
        )

        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind("<Return>", self.send_message)

        # Send button
        tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 11),
            bg="#4CAF50",
            fg="#FFFFFF",
            activebackground="#45A049"
        ).pack(side=tk.LEFT, padx=5)

        # Clear button
        tk.Button(
            root,
            text="Clear Chat",
            command=self.clear_chat,
            font=("Arial", 11),
            bg="#F44336",
            fg="#FFFFFF",
            activebackground="#D32F2F"
        ).pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip()

        if not user_input:
            return

        score, response = get_response(user_input)

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match confidence: {score:.2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)

        self.chat_area.insert(
            tk.END,
            "Welcome to the Technology Chatbot!\n"
            "Ask about technology (e.g., 'my WiFi is slow', 'recommend a laptop', or 'programming help').\n"
        )

        self.chat_area.config(state='disabled')

def Main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    Main()
