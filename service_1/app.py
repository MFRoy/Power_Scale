from application import app, db

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True, host='0.0.0.0')