const socket = io.connect('http://localhost:5000');

socket.on('event_data', (data) => {
    const eventStatus = document.getElementById('event-status');
    const flags = data.feature_flags;

    if (flags["boss_battle_enabled"]) {
        eventStatus.innerHTML = "Boss battle is live!";
    } else if (flags["double_xp_enabled"]) {
        eventStatus.innerHTML = "Double XP is active!";
    } else {
        eventStatus.innerHTML = "No special events active right now.";
    }
});

socket.on('vote_event', (data) => {
    alert(`Event ${data.event} has been voted on!`);
});

document.getElementById('vote-btn').addEventListener('click', () => {
    const event = "boss_battle"; // Example event
    fetch('/api/vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ event })
    }).then(response => response.json())
      .then(data => console.log(data));
});

function updateLeaderboard() {
    fetch('/api/leaderboard')
        .then(response => response.json())
        .then(leaderboard => {
            const leaderboardList = document.getElementById('leaderboard-list');
            leaderboardList.innerHTML = '';
            leaderboard.forEach(player => {
                const li = document.createElement('li');
                li.textContent = `${player.player}: ${player.score}`;
                leaderboardList.appendChild(li);
            });
        });
}

setInterval(updateLeaderboard, 3000); // Update every 3 seconds
