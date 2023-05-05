import {useState, useEffect} from "react"

export function Home (){
    const [resto,setResto]=useState()

    useEffect(() => {
        const fetchResto= async () =>{
            const response=await fetch("http://172.20.10.2:5000/api/FindResto?grocery=chicken&location=montreal");
            const data= await response.json(); //json is the data shared among all
            setResto(data);


        }
        fetchResto();
    })
    return <p>{resto}</p>

}