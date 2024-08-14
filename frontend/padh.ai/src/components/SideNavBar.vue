<template>
  <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-dark sidebar collapse" style="">
    <div class="position-sticky pt-3">
      <h6 class="d-flex justify-content-between align-items-center ps-1 mt-4 mb-1">
        <a class="nav-link active" aria-current="page" href="#">Top Songs</a>
      </h6>
      <ul class="nav flex-column mb-2" v-if="topSongs">
        <!-- showing top 5 songs -->
        <li class="nav-item" v-for="(value, key) in topSongs">
          <a class="nav-link" :href=getSongLink(key) style="text-transform:capitalize;">{{ value.song_name }}</a>
        </li>
      </ul>
      <ul class="nav flex-column mb-3" v-else>
        <li class="nav-item">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <p>There aren't any Songs that has been rated.</p>
          </h6>
        </li>
      </ul>
      <h6 class="d-flex justify-content-between align-items-center ps-1 mt-4 mb-1">
        <a class="nav-link active" aria-current="page" href="#">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" stroke="currentColor"
            stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"
            aria-hidden="true">
            <path
              d="M20 2H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 5h-3v5.5c0 1.38-1.12 2.5-2.5 2.5S10 13.88 10 12.5s1.12-2.5 2.5-2.5c.57 0 1.08.19 1.5.51V5h4v2zM4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6z" />
          </svg>
          Playlists
          <a class="link-secondary" href="/playlist/new" aria-label="Add a new report">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none"
              stroke="var(--bp-khaki)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
              class="feather feather-plus-circle" aria-hidden="true">
              <line x1="12" y1="8" x2="12" y2="16"></line>
              <line x1="8" y1="12" x2="16" y2="12"></line>
            </svg>
          </a>
        </a>
      </h6>
      <ul class="nav flex-column mb-3" v-if="playlists">
        <li class="nav-item" v-for="(value, key) in playlists">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <a :href="getPlaylistLink(key)" class="nav-link" >{{ value.playlist_name }}</a>
          </h6>
        </li>
      </ul>
      <ul class="nav flex-column mb-3" v-else>
        <li class="nav-item">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <p>You don't have any playlists.</p>
          </h6>
        </li>
        <li class="nav-item">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <span>add new playlist</span>
          </h6>
        </li>
      </ul>
    </div>
  </nav>
</template>
<script>
export default {
  name: 'SideNavBar',
  data: function () {
    return {
      playlists: null,
      topSongs: null,
    }
  },
  async beforeMount() {
    await fetch(__API_URL__ + 'user/' + localStorage.getItem('username') + '/playlists', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data === 'No playlists found') {
          this.playlists = null;
        }
        else {
          this.playlists = JSON.parse(data);
        }
      });
    await fetch(__API_URL__ + 'songs?sort_by=rating&limit=5', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data != {}) {
          this.topSongs = data;
        }
      });
  },
  methods: {
    getPlaylistLink(playlistID) {
      return '/playlist/' + playlistID;
    },
    getSongLink(songID) {
      return '/song/' + songID;
    }
  
  }
}
</script>
<style>
.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  padding: 48px 0 0;
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
  overflow-x: hidden;
  overflow-y: auto;
  /* Hide scrollbar for IE, Edge and Firefox */
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.sidebar::-webkit-scrollbar {
  display: none;
}

@media (max-width: 767.98px) {
  .sidebar {
    top: 5rem;
  }
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: hidden;
}

.sidebar .nav-link {
  font-weight: 500;
  color: #fff;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: var(--bp-khaki);
}

.sidebar .nav-link.active {
  color: var(--bp-khaki);
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: var(--bp-khaki);
}

.sidebar a:hover {
  color: var(--bp-khaki);
}
</style>