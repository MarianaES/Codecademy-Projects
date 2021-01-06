import React from 'react';
import Track from '../Track/Track';
import './TrackList.css';

function TrackList(props) {
  console.log(props.tracks)
  return (
    <div className="TrackList">
      {props.tracks.map(track => {
        const {name, artist, album, id} = track;
        return <Track track={track} key={track.id} />})
      }
    </div>
  );
}

export default TrackList;
