# import threading
# from app import app

# def run_flask():
#     app.run(debug=True, use_reloader=False)

# if __name__ == "__main__":
#     # Start Flask app in a new thread
#     flask_thread = threading.Thread(target=run_flask)
#     flask_thread.start()

#     # Your console app code here
#     print("Console app is running. Flask app has been started in another thread.")
#     # Perform other tasks here, or wait for the Flask thread to complete:
#     flask_thread.join()