<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crop Disease Detection</title>
    <style>
        /* General body styling */
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: url('https://img.freepik.com/free-photo/flat-lay-transparent-leaves-lamina_23-2148678504.jpg?t=st=1723920846~exp=1723924446~hmac=adad70b50a08734c662e9c64cb6dc533a2f024d26bbbd0a2a24edc5948446e5d&w=996') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
        }

        /* Container styling */
        .form-container {
            width: 80%;
            max-width: 500px;
            background: linear-gradient(135deg, #b7b5b529, #ffffff, #b7b5b55c);
            border-radius: 20px;
            box-shadow: 0 20px 30px rgba(0, 0, 0, 0.3);
            text-align: center;
            animation: fadeIn 1s ease-in-out;
            backdrop-filter: blur(10px);
            transition: transform 0.3s;
        }

        .form-container:hover {
            transform: scale(1.03);
        }

        .header {
            text-align: center;
            padding: 15px 0;
            background-color: #8ae9b3;
            background-image: linear-gradient(315deg, #c8d6e5 0%, #8ae9b3 74%);
            color: #2c3e50;
            margin-bottom: 20px;
            border-radius: 20px;
        }

        .header h2 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            letter-spacing: 1px;
        }

        form {
            margin-bottom: 20px;
            padding: 0 20px;
        }

        /* Error message styling */
        .error-message {
            color: red;
            font-weight: bold;
            margin-bottom: 15px;
        }

        /* Hide the default file input */
        input[type="file"] {
            display: none;
        }

        /* Custom file input styling */
        .custom-file-upload {
            width: 100%;
            max-width: 300px;
            padding: 10px;
            border-radius: 25px;
            background-color: #42ef8d;
            color: #000;
            cursor: pointer;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
            font-size: 1rem;
            margin-top: 10px;
            margin-bottom: 20px;
            display: inline-block;
            text-align: center;
        }

        .custom-file-upload:hover {
            background-color: #8ae9b3;
            transform: scale(1.03);
        }

        /* Button styling */
        button {
            width: 100%;
            max-width: 320px;
            padding: 10px;
            border-radius: 25px;
            background-color: #42ef8d;
            color: #000;
            border: none;
            cursor: pointer;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
            font-size: 1rem;
            margin-top: 10px;
            margin-bottom: 20px;
            display: inline-block;
            text-align: center;
        }

        button:hover {
            background-color: #8ae9b3;
            transform: scale(1.03);
        }

        /* Fade-in animation */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: scale(0.9);
            }

            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        /* Media queries for smaller screens */
        @media (max-width: 768px) {
            .header h2 {
                font-size: 22px;
            }

            .custom-file-upload,
            button {
                font-size: 0.9rem;
            }
        }

        @media (max-width: 480px) {
            .header h2 {
                font-size: 20px;
            }

            .form-container {
                width: 90%;
            }

            .custom-file-upload,
            button {
                font-size: 0.85rem;
            }
        }
    </style>
</head>

<body>
    <div class="form-container">
        <div class="header">
            <h2>Upload Image</h2>
        </div>
        <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {% if error %}
                <div class="error-message">{{ error }}</div>
            {% endif %}
            <label class="custom-file-upload">
                <input type="file" name="image" id="fileInput">
                <span id="fileName">Choose File</span>
            </label>
            <button type="submit">Upload Image</button>
        </form>
    </div>

    <script>
        const fileInput = document.getElementById('fileInput');
        const fileName = document.getElementById('fileName');

        fileInput.addEventListener('change', function () {
            if (fileInput.files.length > 0) {
                fileName.textContent = fileInput.files[0].name;
            } else {
                fileName.textContent = 'Choose File';
            }
        });
    </script>
</body>

</html>
