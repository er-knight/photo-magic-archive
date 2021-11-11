# Photo Magic
Programming Assignment based on Linear Feedback Shift Register using Python

## Basic Setup
- Clone Repository (Using SSH)
    ```sh
    git clone git@github.com:er-knight/photo-magic.git
    ```
- <details> 
    <summary>Clone Repository (Using HTTPS)</summary>

    ```sh
    git clone https://github.com/er-knight/photo-magic.git
    ```
</details>

- Change Directory to `photo-magic`
    ```sh
    cd photo-magic
    ```

- Create Virtual Environment
    ```sh
    python3 -m venv venv
    ```

- Activate Virtual Environment (Bash on Linux)
    ```sh
    source venv/bin/activate
    ``` 
- <details> 
    <summary>Activate Virtual Environment (PowerShell on Windows)</summary>

    ```ps
    PS C:\> venv\Scripts\Activate.ps1
    ```
</details>
    
- Install Requirements
    ```sh
    python3 -m pip install -r requirements.txt
    ```

- Build `lfsr` Extension
    ```
    python3 setup.py build_ext --inplace
    ```
    *Note: [On Windows, to build an Extension Module, Microsoft Visual C/C++ (MSVC) is required.](https://cython.readthedocs.io/en/latest/src/quickstart/install.html)*

## Encrypt Image  
```sh
python3 main.py --encrypt --image-path=<image-path> --password=<password> --tap-code=<tap-code>
```

## Decrypt Image  
```sh
python3 main.py --decrypt --image-path=<image-path> --password=<password> --tap-code=<tap-code>
```

## Reference
- [Random Numbers with Linear Feedback Shift Register by Computerphile (YouTube)](https://youtu.be/Ks1pw1X22y4)
- [Assignment based on Linear Feedback Shift Register](https://www.cs.princeton.edu/courses/archive/fall10/cos126/assignments/lfsr.html)
