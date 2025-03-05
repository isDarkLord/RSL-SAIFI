# Remote Screen Logger

A simple remote screen capture system using Python that allows a client to capture and send screenshots to a server over a network.

## Features

- Capture screenshots remotely
- Send and display screenshots in real-time
- Works over a local network or the same machine (localhost)

## Installation & Setup (Windows)

### 1️. Clone the Repository

```bash
git clone https://github.com/hammad-saifi/RSL-SAIFI.git
cd RSL-SAIFI
```

### 2️. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Activate virtual environment (Windows)
```

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Server

1. Open a terminal in the project directory.
2. Run the server script:

```bash
python server.py
```

### Run the Client

1. Open another terminal in the same directory.
2. Update `client.py` with the correct IP address (use `127.0.0.1` if running on the same PC).
3. Run the client script:

```bash
python client.py
```

## Running on One PC vs Two PCs

### Using on One PC

1. Set the server IP in `client.py` to `127.0.0.1` (localhost):
   ```python
   host_ip = '127.0.0.1'
   ```
2. Run `server.py` in one terminal and `client.py` in another.

### Using on Two PCs

1. Find the IP address of the server PC:
   - Open Command Prompt (`cmd`) and run:
     ```bash
     ipconfig
     ```
   - Look for `IPv4 Address` (e.g., `192.168.1.100`).
2. Set this IP in `client.py`:
   ```python
   host_ip = '192.168.X.XXX'  # Replace with actual server IP
   ```
3. Run `server.py` on the **server PC**.
4. Run `client.py` on the **client PC**.

## 🛠 Troubleshooting

### ❌ PyAutoGUI Import Error

If you see an error related to `pyautogui` or `pyscreeze`, try installing the missing dependencies:

```bash
pip install pyautogui pyscreeze pillow
```

### ❌ Connection Issues

- Ensure the server is running before starting the client.
- Use the correct IP address for the server.
- Check your firewall settings (allow Python to communicate over the network).

## 📜 License

this project is a clone of [medium](https\://medium.com/@boata.andrei88/building-a-simple-remote-screen-capture-system-using-python-%EF%B8%8F-4f83dbf6f7bd)



## 📧 Contact

```saifi123hasan@gmail.com```

For any issues, contact [Saifi Hasan](https://saifi01.netlify.app).

