# 🎰 Multiplayer Roulette Game

## 📝 Overview
This is a **real-time multiplayer roulette game** built with **Flask-SocketIO** for backend logic and **Three.js** for stunning 3D visuals. Players can join, place bets, and watch a realistic roulette wheel spin in their browser.

## 📂 Directory Structure
```
/flask_roulette_game
│── app.py                     # Flask-SocketIO Backend
│── requirements.txt            # Dependencies
│── templates/
│   ├── index.html              # Main game UI (HTML + JavaScript)
│── static/
│   ├── roulette.js             # Three.js 3D Roulette Wheel
│   ├── styles.css              # CSS for Styling
│── README.md                   # Instructions
```

## 🚀 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/flask-roulette-game.git
cd flask-roulette-game
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```

### 4️⃣ Open the Game in Your Browser
- Visit `http://localhost:5000`
- Players can **place bets** and **spin the wheel** in real-time.

## 🕹️ How to Play
1. **Join the game** - Each player starts with **100 chips**.
2. **Place bets** - Choose a number and bet some chips.
3. **No More Bets!** - The dealer locks the bets.
4. **Watch the wheel spin** - The winning number is revealed.
5. **Winners get paid** - Players earn **35x** their bet if they win!
6. **Start the next round** - Repeat!

## 🎨 Tech Stack
- **Backend:** Flask + Flask-SocketIO (Python)
- **Frontend:** Three.js (WebGL for 3D Roulette)
- **Multiplayer:** WebSockets (real-time updates)
- **Styling:** CSS

## 🌍 Deployment
This game can be hosted on:
- **Railway.app** (free Flask hosting)
- **Linode / DigitalOcean** (VPS self-hosting)
- **Vercel** (for the frontend if using React)

## 🤝 Contributing
Want to improve the game? Feel free to fork and contribute!

## 🛠️ Future Enhancements
- 🎭 **3D animated dealer placing bets**
- 🎲 **Clickable roulette board for betting**
- 📱 **Mobile-responsive version**

## 📜 License
MIT License

---
🚀 Enjoy the game! Let me know if you need additional features. 🎰🔥

