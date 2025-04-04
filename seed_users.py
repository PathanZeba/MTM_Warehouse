from app import create_app, db
from app.models.user import User
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = create_app()

with app.app_context():
    try:
        
        db.session.query(User).delete()
        db.session.commit()  

        password = "admin"
        password_hash = generate_password_hash(password)  

        
        superuser = User(
            Id=str(uuid.uuid4()),  
            Username="superuser",
            NormalizedUsername="SUPERUSER",
            Email="superuser@example.com",  
            NormalizedEmail="SUPERUSER@EXAMPLE.COM",
            EmailConfirmed=False,
            PasswordHash=password_hash,
            SecurityStamp=str(uuid.uuid4()),
            ConcurrencyStamp=str(uuid.uuid4()),
            PhoneNumber=None,
            PhoneNumberConfirmed=False,
            TwoFactorEnabled=False,
            LockoutEnd=None,
            LockoutEnabled=True,
            AccessFailedCount=0
        )

        
        masteruser = User(
            Id=str(uuid.uuid4()),  
            Username="masteruser",
            NormalizedUsername="MASTERUSER",
            Email="masteruser@example.com",  
            NormalizedEmail="MASTERUSER@EXAMPLE.COM",
            EmailConfirmed=False,
            PasswordHash=password_hash,
            SecurityStamp=str(uuid.uuid4()),
            ConcurrencyStamp=str(uuid.uuid4()),
            PhoneNumber=None,
            PhoneNumberConfirmed=False,
            TwoFactorEnabled=False,
            LockoutEnd=None,
            LockoutEnabled=True,
            AccessFailedCount=0
        )

        db.session.add(superuser)
        db.session.add(masteruser)
        db.session.commit()

        print(f" Superuser created with Id: {superuser.Id}")
        print(f" Masteruser created with Id: {masteruser.Id}")

        
        stored_user = db.session.query(User).filter_by(Username="superuser").first()

        if stored_user:
            print(f" Stored Hash in DB: {stored_user.PasswordHash}")

            if check_password_hash(stored_user.PasswordHash, password):
                print(" Password verification successful!")
            else:
                print(" Password verification failed!")

    except Exception as e:
        db.session.rollback()
        print(f" Error during user creation: {e}")

    finally:
        db.session.close()
