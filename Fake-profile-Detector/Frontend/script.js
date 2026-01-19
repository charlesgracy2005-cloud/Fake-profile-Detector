function analyze() {
    let profileUrl = document.getElementById("profileUrl").value;
    let imageUrl = document.getElementById("imageUrl").value;

    if (profileUrl === "" || imageUrl === "") {
        alert("Please fill all fields");
        return;
    }

    document.getElementById("result").innerHTML =
        "<p>Backend analysis is done via Python script.</p>";
}
