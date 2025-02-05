// Create the 3D Roulette Wheel using Three.js
import * as THREE from 'three';

let scene, camera, renderer, wheel;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Load the roulette wheel
    let geometry = new THREE.CylinderGeometry(5, 5, 1, 36);
    let material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    wheel = new THREE.Mesh(geometry, material);
    scene.add(wheel);

    camera.position.z = 10;
    animate();
}

function animate() {
    requestAnimationFrame(animate);
    wheel.rotation.y += 0.01;  // Spin effect
    renderer.render(scene, camera);
}

init();