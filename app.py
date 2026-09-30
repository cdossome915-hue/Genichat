from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Genichat</title>

<style>
*{
    box-sizing:border-box;
    margin:0;
    padding:0;
    font-family:Arial,sans-serif;
}

body{
    background:#f4f5f7;
    color:#171717;
    height:100vh;
    overflow:hidden;
}

body.dark{
    background:#111318;
    color:#fff;
}

button{
    border:0;
    cursor:pointer;
}

.screen{
    display:none;
    width:100%;
    height:100vh;
}

.screen.active{
    display:flex;
}

/* ================= LOGIN ================= */

.auth{
    align-items:center;
    justify-content:center;
    padding:20px;
}

.auth-box{
    width:100%;
    max-width:420px;
    background:white;
    border-radius:25px;
    padding:30px 22px;
    box-shadow:0 10px 40px #0002;
}

.dark .auth-box{
    background:#1d2028;
}

.logo{
    text-align:center;
    font-size:38px;
    font-weight:bold;
    margin-bottom:8px;
}

.logo span{
    color:#6757e8;
}

.subtitle{
    text-align:center;
    color:#777;
    margin-bottom:25px;
}

.input{
    width:100%;
    padding:15px;
    border:1px solid #ddd;
    border-radius:13px;
    margin-bottom:12px;
    outline:none;
    font-size:15px;
}

.dark .input{
    background:#292d36;
    color:white;
    border-color:#444;
}

.primary{
    width:100%;
    background:#6757e8;
    color:white;
    padding:15px;
    border-radius:13px;
    font-weight:bold;
    font-size:16px;
}

.secondary{
    width:100%;
    margin-top:10px;
    padding:14px;
    border-radius:13px;
    background:#eee;
}

.dark .secondary{
    background:#30343d;
    color:white;
}

.error{
    color:#e53935;
    text-align:center;
    margin:10px 0;
    min-height:20px;
}

/* ================= APP ================= */

.app{
    flex-direction:column;
}

.topbar{
    height:65px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 17px;
    background:white;
    border-bottom:1px solid #eee;
}

.dark .topbar{
    background:#1a1d24;
    border-color:#292d36;
}

.brand{
    font-size:25px;
    font-weight:bold;
}

.brand span{
    color:#6757e8;
}

.icon-btn{
    width:42px;
    height:42px;
    border-radius:50%;
    background:#f0f0f3;
    font-size:19px;
}

.dark .icon-btn{
    background:#30343d;
    color:white;
}

.content{
    flex:1;
    overflow:auto;
    padding-bottom:80px;
}

.page{
    display:none;
    padding:18px;
}

.page.active{
    display:block;
}

.section-title{
    font-size:24px;
    font-weight:bold;
    margin-bottom:15px;
}

.empty{
    text-align:center;
    color:#888;
    padding:70px 20px;
}

.contact{
    display:flex;
    align-items:center;
    padding:13px;
    margin-bottom:9px;
    border-radius:17px;
    background:white;
    cursor:pointer;
}

.dark .contact{
    background:#1d2028;
}

.avatar{
    width:52px;
    height:52px;
    border-radius:50%;
    object-fit:cover;
    background:#6757e8;
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:bold;
    margin-right:12px;
}

.contact-name{
    font-weight:bold;
}

.status{
    color:#777;
    font-size:13px;
    margin-top:4px;
}

/* ================= BOTTOM ================= */

.bottom{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    height:70px;
    display:flex;
    justify-content:space-around;
    align-items:center;
    background:white;
    border-top:1px solid #ddd;
}

.dark .bottom{
    background:#1a1d24;
    border-color:#292d36;
}

.nav-btn{
    background:transparent;
    color:#777;
    font-size:12px;
    text-align:center;
}

.nav-btn.active{
    color:#6757e8;
    font-weight:bold;
}

.nav-icon{
    display:block;
    font-size:22px;
    margin-bottom:3px;
}

/* ================= ADD CONTACT ================= */

.add-box{
    background:white;
    padding:20px;
    border-radius:20px;
}

.dark .add-box{
    background:#1d2028;
}

.code{
    font-size:20px;
    font-weight:bold;
    text-align:center;
    padding:15px;
    background:#f0efff;
    border-radius:15px;
    margin:15px 0;
    color:#6757e8;
}

/* ================= CHAT ================= */

.chat{
    flex-direction:column;
    background:#f5f5f6;
}

.dark .chat{
    background:#111318;
}

.chat-head{
    height:65px;
    display:flex;
    align-items:center;
    padding:0 12px;
    background:white;
}

.dark .chat-head{
    background:#1a1d24;
}

.back{
    font-size:25px;
    background:transparent;
    margin-right:12px;
}

.chat-user{
    font-weight:bold;
}

.messages{
    flex:1;
    overflow:auto;
    padding:18px 12px 90px;
}

.msg{
    max-width:78%;
    padding:11px 14px;
    margin:6px 0;
    border-radius:17px;
    word-wrap:break-word;
}

.mine{
    margin-left:auto;
    background:#6757e8;
    color:white;
    border-bottom-right-radius:5px;
}

.theirs{
    background:white;
    border-bottom-left-radius:5px;
}

.dark .theirs{
    background:#292d36;
}

.chat-input{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    display:flex;
    gap:8px;
    padding:10px;
    background:white;
}

.dark .chat-input{
    background:#1a1d24;
}

.chat-input input{
    flex:1;
    padding:14px;
    border-radius:22px;
    border:1px solid #ddd;
}

.dark .chat-input input{
    background:#292d36;
    color:white;
}

.send{
    width:48px;
    height:48px;
    border-radius:50%;
    background:#6757e8;
    color:white;
}

/* ================= PROFILE ================= */

.profile{
    text-align:center;
}

.big-avatar{
    width:110px;
    height:110px;
    border-radius:50%;
    object-fit:cover;
    background:#6757e8;
    margin:10px auto 15px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:35px;
}

.card{
    background:white;
    border-radius:20px;
    padding:18px;
    margin-top:15px;
}

.dark .card{
    background:#1d2028;
}

.setting{
    padding:16px 5px;
    border-bottom:1px solid #ddd;
    display:flex;
    justify-content:space-between;
}

.dark .setting{
    border-color:#333;
}

/* ================= STATUS ================= */

.status-card{
    background:white;
    border-radius:20px;
    padding:18px;
    margin-bottom:15px;
}

.dark .status-card{
    background:#1d2028;
}

.status-add{
    background:#6757e8;
    color:white;
    padding:14px;
    border-radius:14px;
    width:100%;
    margin-bottom:15px;
}

/* ================= MODAL ================= */

.modal{
    display:none;
    position:fixed;
    inset:0;
    background:#0008;
    align-items:center;
    justify-content:center;
    padding:20px;
    z-index:100;
}

.modal.show{
    display:flex;
}

.modal-box{
    width:100%;
    max-width:420px;
    background:white;
    border-radius:25px;
    padding:22px;
}

.dark .modal-box{
    background:#1d2028;
}

.close{
    float:right;
    background:transparent;
    font-size:25px;
}
</style>
</head>

<body>

<!-- ================= AUTH ================= -->

<section id="auth" class="screen auth active">

<div class="auth-box">

<div class="logo">
    geni<span>chat</span>
</div>

<div class="subtitle">
    Discute avec tes contacts
</div>

<div id="authError" class="error"></div>

<input id="username"
       class="input"
       placeholder="Nom utilisateur">

<input id="displayName"
       class="input"
       placeholder="Nom affiché">

<input id="password"
       class="input"
       type="password"
       placeholder="Mot de passe">

<button class="primary"
        onclick="register()">
Créer mon compte
</button>

<button class="secondary"
        onclick="login()">
J'ai déjà un compte
</button>

</div>
</section>


<!-- ================= APP ================= -->

<section id="app" class="screen app">

<header class="topbar">

<div class="brand">
geni<span>chat</span>
</div>

<button class="icon-btn"
        onclick="openSettings()">
⚙️
</button>

</header>


<main class="content">

<!-- ACCUEIL -->

<div id="home" class="page active">

<div class="section-title">
Contacts
</div>

<div id="contacts"></div>

</div>


<!-- AJOUT -->

<div id="add" class="page">

<div class="section-title">
Ajouter un contact
</div>

<div class="add-box">

<p>
Entre le code Genichat de ton ami.
</p>

<input id="friendCode"
       class="input"
       placeholder="MALI-XXXX-XXXX">

<button class="primary"
        onclick="addContact()">
Ajouter
</button>

<div id="addError"
     class="error">
</div>

</div>

</div>


<!-- STATUS -->

<div id="status" class="page">

<div class="section-title">
Statuts
</div>

<button class="status-add"
        onclick="createStatus()">
＋ Ajouter un statut
</button>

<div class="status-card">
    <b>Statuts 24 h</b>
    <p class="status">
    Les statuts de tes contacts apparaîtront ici.
    </p>
</div>

</div>


<!-- PROFIL -->

<div id="profile" class="page">

<div class="profile">

<div id="profileAvatar"
     class="big-avatar">
?
</div>

<h2 id="profileName">
-
</h2>

<p id="profileUsername"
   class="status">
-
</p>

<div class="code"
     id="myCode">
-
</div>

<div class="card">

<input id="newDisplayName"
       class="input"
       placeholder="Nouveau nom">

<input id="newBio"
       class="input"
       placeholder="Bio">

<button class="primary"
        onclick="updateProfile()">
Enregistrer
</button>

</div>

</div>

</div>

</main>


<nav class="bottom">

<button class="nav-btn active"
        onclick="showPage('home',this)">
<span class="nav-icon">💬</span>
Accueil
</button>

<button class="nav-btn"
        onclick="showPage('add',this)">
<span class="nav-icon">➕</span>
Ajouter
</button>

<button class="nav-btn"
        onclick="showPage('status',this)">
<span class="nav-icon">⭕</span>
Statuts
</button>

<button class="nav-btn"
        onclick="showPage('profile',this)">
<span class="nav-icon">👤</span>
Profil
</button>

</nav>

</section>


<!-- ================= CHAT ================= -->

<section id="chat"
         class="screen chat">

<header class="chat-head">

<button class="back"
        onclick="closeChat()">
‹
</button>

<div id="chatAvatar"
     class="avatar">
?
</div>

<div>
<div id="chatName"
     class="chat-user">
-
</div>

<div id="chatStatus"
     class="status">
-
</div>
</div>

</header>

<div id="messages"
     class="messages">
</div>

<div class="chat-input">

<input id="messageInput"
       placeholder="Écrire un message..."
       onkeydown="if(event.key==='Enter')sendMessage()">

<button class="send"
        onclick="sendMessage()">
➤
</button>

</div>

</section>


<!-- ================= SETTINGS ================= -->

<div id="settingsModal"
     class="modal">

<div class="modal-box">

<button class="close"
        onclick="closeSettings()">
×
</button>

<h2>Paramètres</h2>

<br>

<div class="setting">
<span>Thème sombre</span>
<input type="checkbox"
       id="darkMode"
       onchange="toggleDark()">
</div>

<div class="setting">
<span>Mon code</span>
<b id="settingsCode">-</b>
</div>

<br>

<button class="secondary"
        onclick="logout()">
Se déconnecter
</button>

</div>

</div>


<script>

/* =========================================================
   GENICHAT
   SERVEUR API
========================================================= */

const API =
"https://campus-messenger-server.onrender.com";

let token =
localStorage.getItem("genichat_token");

let currentUser = null;
let currentContact = null;
let socket = null;


/* =========================================================
   API
========================================================= */

async function api(
    path,
    options={}
){

    options.headers =
        options.headers || {};

    if(token){

        options.headers[
            "Authorization"
        ] =
            "Bearer " + token;
    }

    if(options.body &&
       typeof options.body !== "string"){

        options.headers[
            "Content-Type"
        ] =
            "application/json";

        options.body =
            JSON.stringify(
                options.body
            );
    }

    const response =
        await fetch(
            API + path,
            options
        );

    let data = {};

    try{
        data =
            await response.json();
    }
    catch(e){}

    if(!response.ok){

        throw new Error(
            data.detail ||
            "Erreur serveur"
        );
    }

    return data;
}


/* =========================================================
   INSCRIPTION
========================================================= */

async function register(){

    const username =
        document.getElementById(
            "username"
        ).value.trim();

    const displayName =
        document.getElementById(
            "displayName"
        ).value.trim();

    const password =
        document.getElementById(
            "password"
        ).value;

    const error =
        document.getElementById(
            "authError"
        );

    error.textContent = "";

    if(
        username.length < 3 ||
        displayName.length < 1 ||
        password.length < 8
    ){

        error.textContent =
            "Nom : 3 caractères minimum. Mot de passe : 8 caractères minimum.";

        return;
    }

    try{

        const data =
            await api(
                "/api/register",
                {
                    method:"POST",
                    body:{
                        username,
                        displayName,
                        password
                    }
                }
            );

        token =
            data.token;

        localStorage.setItem(
            "genichat_token",
            token
        );

        await loadMe();

        enterApp();

    }
    catch(e){

        error.textContent =
            e.message;
    }
}


/* =========================================================
   CONNEXION
========================================================= */

async function login(){

    const username =
        document.getElementById(
            "username"
        ).value.trim();

    const password =
        document.getElementById(
            "password"
        ).value;

    const error =
        document.getElementById(
            "authError"
        );

    error.textContent = "";

    try{

        const data =
            await api(
                "/api/login",
                {
                    method:"POST",
                    body:{
                        username,
                        password
                    }
                }
            );

        token =
            data.token;

        localStorage.setItem(
            "genichat_token",
            token
        );

        await loadMe();

        enterApp();

    }
    catch(e){

        error.textContent =
            e.message;
    }
}


/* =========================================================
   MON PROFIL
========================================================= */

async function loadMe(){

    const data =
        await api("/api/me");

    currentUser =
        data.user;

    document.getElementById(
        "profileName"
    ).textContent =
        currentUser.displayName;

    document.getElementById(
        "profileUsername"
    ).textContent =
        "@" + currentUser.username;

    document.getElementById(
        "myCode"
    ).textContent =
        currentUser.code;

    document.getElementById(
        "settingsCode"
    ).textContent =
        currentUser.code;

    document.getElementById(
        "newDisplayName"
    ).value =
        currentUser.displayName;

    document.getElementById(
        "newBio"
    ).value =
        currentUser.bio || "";

    setAvatar(
        document.getElementById(
            "profileAvatar"
        ),
        currentUser
    );
}


/* =========================================================
   ENTRER DANS GENICHAT
========================================================= */

async function enterApp(){

    document.getElementById(
        "auth"
    ).classList.remove("active");

    document.getElementById(
        "app"
    ).classList.add("active");

    await loadContacts();

    connectSocket();
}


/* =========================================================
   CONTACTS
========================================================= */

async function loadContacts(){

    const container =
        document.getElementById(
            "contacts"
        );

    try{

        const data =
            await api(
                "/api/contacts"
            );

        container.innerHTML = "";

        if(
            !data.contacts ||
            data.contacts.length === 0
        ){

            container.innerHTML =
                `<div class="empty">
                    Aucun contact pour le moment.<br><br>
                    Utilise « Ajouter » pour ajouter un ami.
                </div>`;

            return;
        }

        data.contacts.forEach(
            contact => {

                const div =
                    document.createElement(
                        "div"
                    );

                div.className =
                    "contact";

                div.onclick =
                    () => openChat(contact);

                const avatar =
                    document.createElement(
                        "div"
                    );

                avatar.className =
                    "avatar";

                setAvatar(
                    avatar,
                    contact
                );

                const info =
                    document.createElement(
                        "div"
                    );

                info.innerHTML =
                    `
                    <div class="contact-name">
                    ${escapeHtml(
                        contact.displayName
                    )}
                    </div>

                    <div class="status">
                    ${
                        contact.online
                        ? "● En ligne"
                        : "Hors ligne"
                    }
                    </div>
                    `;

                div.appendChild(
                    avatar
                );

                div.appendChild(
                    info
                );

                container.appendChild(
                    div
                );
            }
        );

    }
    catch(e){

        container.innerHTML =
            `<div class="empty">
            ${escapeHtml(e.message)}
            </div>`;
    }
}


/* =========================================================
   AJOUT CONTACT
========================================================= */

async function addContact(){

    const input =
        document.getElementById(
            "friendCode"
        );

    const error =
        document.getElementById(
            "addError"
        );

    const code =
        input.value
            .trim()
            .toUpperCase();

    error.textContent = "";

    if(!code){

        error.textContent =
            "Entre le code de ton ami.";

        return;
    }

    try{

        await api(
            "/api/contacts",
            {
                method:"POST",
                body:{code}
            }
        );

        input.value = "";

        showPage(
            "home",
            document.querySelector(
                ".nav-btn"
            )
        );

        await loadContacts();

    }
    catch(e){

        error.textContent =
            e.message;
    }
}


/* =========================================================
   CHAT
========================================================= */

async function openChat(contact){

    currentContact =
        contact;

    document.getElementById(
        "app"
    ).classList.remove("active");

    document.getElementById(
        "chat"
    ).classList.add("active");

    document.getElementById(
        "chatName"
    ).textContent =
        contact.displayName;

    document.getElementById(
        "chatStatus"
    ).textContent =
        contact.online
        ? "En ligne"
        : "Hors ligne";

    setAvatar(
        document.getElementById(
            "chatAvatar"
        ),
        contact
    );

    await loadMessages();
}


function closeChat(){

    document.getElementById(
        "chat"
    ).classList.remove("active");

    document.getElementById(
        "app"
    ).classList.add("active");
}


/* =========================================================
   HISTORIQUE
========================================================= */

async function loadMessages(){

    if(!currentContact)
        return;

    const container =
        document.getElementById(
            "messages"
        );

    container.innerHTML = "";

    try{

        const data =
            await api(
                "/api/messages/" +
                currentContact.id
            );

        data.messages.forEach(
            message => {

                addMessageToScreen(
                    message
                );
            }
        );

        scrollMessages();

    }
    catch(e){

        container.innerHTML =
            `<div class="empty">
            ${escapeHtml(e.message)}
            </div>`;
    }
}


/* =========================================================
   ENVOYER MESSAGE
========================================================= */

function sendMessage(){

    const input =
        document.getElementById(
            "messageInput"
        );

    const text =
        input.value.trim();

    if(!text ||
       !currentContact ||
       !socket)
        return;

    socket.send(
        JSON.stringify({
            event:"message",
            receiverId:
                currentContact.id,
            text:text
        })
    );

    input.value = "";
}


/* =========================================================
   WEBSOCKET
========================================================= */

function connectSocket(){

    if(!token)
        return;

    let websocketUrl =
        API.replace(
            "https://",
            "wss://"
        ).replace(
            "http://",
            "ws://"
        );

    websocketUrl +=
        "/ws?token=" +
        encodeURIComponent(token);

    socket =
        new WebSocket(
            websocketUrl
        );

    socket.onopen = () => {

        console.log(
            "Genichat connecté"
        );
    };

    socket.onmessage =
        event => {

            try{

                const data =
                    JSON.parse(
                        event.data
                    );

                if(
                    data.event ===
                    "message"
                ){

                    if(
                        currentContact &&
                        (
                            data.senderId ===
                            currentContact.id
                            ||
                            data.receiverId ===
                            currentContact.id
                        )
                    ){

                        addMessageToScreen(
                            data
                        );

                        scrollMessages();
                    }
                }

            }
            catch(e){

                console.log(e);
            }
        };

    socket.onclose = () => {

        console.log(
            "WebSocket fermé"
        );

        setTimeout(
            connectSocket,
            3000
        );
    };
}


/* =========================================================
   AFFICHER MESSAGE
========================================================= */

function addMessageToScreen(
    message
){

    const container =
        document.getElementById(
            "messages"
        );

    const div =
        document.createElement(
            "div"
        );

    const mine =
        message.senderId ===
        currentUser.id;

    div.className =
        "msg " +
        (
            mine
            ? "mine"
            : "theirs"
        );

    div.textContent =
        message.text;

    container.appendChild(
        div
    );
}


function scrollMessages(){

    const box =
        document.getElementById(
            "messages"
        );

    box.scrollTop =
        box.scrollHeight;
}


/* =========================================================
   PROFIL
========================================================= */

async function updateProfile(){

    try{

        const displayName =
            document.getElementById(
                "newDisplayName"
            ).value.trim();

        const bio =
            document.getElementById(
                "newBio"
            ).value.trim();

        const data =
            await api(
                "/api/me",
                {
                    method:"PATCH",
                    body:{
                        displayName,
                        bio
                    }
                }
            );

        currentUser =
            data.user;

        await loadMe();

        alert(
            "Profil enregistré."
        );

    }
    catch(e){

        alert(e.message);
    }
}


/* =========================================================
   PARAMÈTRES
========================================================= */

function openSettings(){

    document.getElementById(
        "settingsModal"
    ).classList.add("show");
}

function closeSettings(){

    document.getElementById(
        "settingsModal"
    ).classList.remove("show");
}

function toggleDark(){

    const enabled =
        document.getElementById(
            "darkMode"
        ).checked;

    document.body.classList.toggle(
        "dark",
        enabled
    );

    localStorage.setItem(
        "genichat_dark",
        enabled
    );
}


/* =========================================================
   NAVIGATION
========================================================= */

function showPage(
    id,
    button
){

    document.querySelectorAll(
        ".page"
    ).forEach(
        page =>
            page.classList.remove(
                "active"
            )
    );

    document.getElementById(
        id
    ).classList.add(
        "active"
    );

    document.querySelectorAll(
        ".nav-btn"
    ).forEach(
        b =>
            b.classList.remove(
                "active"
            )
    );

    if(button)
        button.classList.add(
            "active"
        );

    if(id === "home")
        loadContacts();
}


/* =========================================================
   STATUT
========================================================= */

function createStatus(){

    alert(
        "La publication de statuts 24 h sera activée dans la prochaine version avec le serveur."
    );
}


/* =========================================================
   AVATAR
========================================================= */

function setAvatar(
    element,
    user
){

    if(user.avatar){

        element.style.backgroundImage =
            `url("${user.avatar}")`;

        element.style.backgroundSize =
            "cover";

        element.style.backgroundPosition =
            "center";

        element.textContent = "";

    }else{

        element.style.backgroundImage =
            "none";

        element.textContent =
            (
                user.displayName ||
                "?"
            )
            .charAt(0)
            .toUpperCase();
    }
}


/* =========================================================
   LOGOUT
========================================================= */

function logout(){

    localStorage.removeItem(
        "genichat_token"
    );

    token = null;

    if(socket){

        socket.close();

        socket = null;
    }

    location.reload();
}


/* =========================================================
   SÉCURITÉ AFFICHAGE
========================================================= */

function escapeHtml(
    text
){

    const div =
        document.createElement(
            "div"
        );

    div.textContent =
        text;

    return div.innerHTML;
}


/* =========================================================
   DÉMARRAGE
========================================================= */

async function start(){

    const dark =
        localStorage.getItem(
            "genichat_dark"
        ) === "true";

    document.body.classList.toggle(
        "dark",
        dark
    );

    document.getElementById(
        "darkMode"
    ).checked =
        dark;

    if(!token)
        return;

    try{

        await loadMe();

        enterApp();

    }
    catch(e){

        localStorage.removeItem(
            "genichat_token"
        );

        token = null;
    }
}

start();

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return {
        "site": "Genichat",
        "status": "online"
    }


if __name__ == "__main__":
    port = int(__import__("os").environ.get("PORT", 10000))
    app.run(
        host="0.0.0.0",
        port=port
    )
"""

app.run(host="0.0.0.0", port=port)
