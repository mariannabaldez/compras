import Link from "next/link";
import Image from "next/image";

import icone from "../public/img/icone.jpeg"

/*const linkStyle = {
    marginRight: 15
};*/
const Home = () => (
    <header>
        <div class="centralizar-cabecalho">
            <Image src={icone}/>
            <div class="titulo-cabecalho"><h2>Lista de compras da Marianna</h2></div>
        </div>    
    </header>
);
export default Home;