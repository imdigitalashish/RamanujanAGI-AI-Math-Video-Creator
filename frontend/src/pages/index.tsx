import React, { useState } from 'react';
import { Cover } from '@/components/ui/cover';
import { PlaceholdersAndVanishInput } from '@/components/ui/vanish-input';
import axios from 'axios';

export default function Home() {
  const [value, setValue] = useState("");
  const [videoID, setVideoID] = useState("");
  const [loading, setLoading] = useState(false); // State to track loading status

  const placeholders = [
    "Permutation and Combination Animation?",
    "A sine curve animationn?",
    "A cos curve animation?",
    "What is Python?",
  ];

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
    setValue(e.target.value);
  };

  const getTheVideo = async () => {
    setLoading(true); // Set loading to true when starting the request
    try {
      const request = await axios.get(`http://localhost:9090/get_the_video?prompt=${value}`);
      const response = await request.data;

      if (response && response.video_name) {
        setVideoID(response.video_name);
      }
      console.log(response);
    } catch (error) {
      console.error("Error fetching video:", error);
    } finally {
      setLoading(false); // Set loading to false after the request completes
    }
  };

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("submitted");
    getTheVideo();
  };

  return (
    <div className='w-full h-[100vh] theme-zinc flex bg-black justify-center items-center'>
      <div className='h-fit'>
        <h1 className="text-4xl md:text-4xl lg:text-6xl font-semibold max-w-7xl mx-auto text-center relative z-20 py-6 bg-clip-text text-transparent bg-gradient-to-b from-neutral-800 via-white to-white">
          Build amazing Math Animation Videos <br /> at <Cover>warp speed</Cover>
        </h1>
        <PlaceholdersAndVanishInput
          placeholders={placeholders}
          onChange={handleChange}
          onSubmit={onSubmit}
        />

        {loading ? (
          <div className="flex justify-center items-center pt-10">
            {/* Loading Spinner */}
            <div className="animate-spin rounded-full h-32 w-32 border-t-4 border-b-4 border-gray-200"></div>
          </div>
        ) : (
          videoID && (
            <video autoPlay controls src={`http://localhost:9090/${videoID}`}></video>
          )
        )}
      </div>
    </div>
  );
}