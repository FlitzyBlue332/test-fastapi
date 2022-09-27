from fastapi import FastAPI
from pydantic import BaseModel

#ganti env: .\env\Scripts\Activate.ps1  

app = FastAPI()


class Mahasiswa(BaseModel):
    nim: str
    name: str

daftarMahasiswa = {"18220031":"Muhammad Raihan Aulia"}

@app.post("/")
async def create_mahasiswa(mahasiswa: Mahasiswa):
    daftarMahasiswa[mahasiswa.nim] = mahasiswa.name
    return mahasiswa

@app.get("/mahasiswa/{nim}")
async def read_mahasiswa(nim):
    return {nim : daftarMahasiswa[nim]}

@app.get("/daftarnim")
async def read_daftar():
    string = ""
    for keys in daftarMahasiswa.keys():
        string = string + " " + keys
    return string