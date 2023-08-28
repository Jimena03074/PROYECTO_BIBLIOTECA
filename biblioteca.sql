-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-04-2023 a las 05:23:30
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acervo`
--

CREATE TABLE `acervo` (
  `codigoA` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `acervo`
--

INSERT INTO `acervo` (`codigoA`, `nombre`, `descripcion`) VALUES
(123456, 'Tecnologia', 'libros de tecnologias'),
(123458, 'Matematicas', 'Libros de matematicas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `contraseña` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`id`, `nombre`, `contraseña`) VALUES
(1, 'jose', '12345678'),
(2, 'edgar', '12345698');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `codigo` int(11) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `autor` varchar(50) NOT NULL,
  `edicion` varchar(50) NOT NULL,
  `editorial` varchar(50) NOT NULL,
  `año` varchar(50) NOT NULL,
  `acervo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`codigo`, `titulo`, `autor`, `edicion`, `editorial`, `año`, `acervo`) VALUES
(1234567890, 'redes', 'pascal', '2', 'salamandra', '2021', 'redes'),
(1234567891, 'neurociencia', 'suzana', '1', 'azteca', '2022', 'ciencia'),
(1234567892, 'programacion', 'Raul', '2', 'mexico', '2023', 'ciencia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `idP` int(11) NOT NULL,
  `matricula` varchar(30) NOT NULL,
  `codigoA` varchar(30) NOT NULL,
  `codigo` varchar(30) NOT NULL,
  `fecha_inicio` varchar(30) NOT NULL,
  `fecha_fin` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`idP`, `matricula`, `codigoA`, `codigo`, `fecha_inicio`, `fecha_fin`) VALUES
(1, '181803074', '123456', '1234567890', '31/03/2023', '31/04/2023');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `renovar`
--

CREATE TABLE `renovar` (
  `IDR` int(30) NOT NULL,
  `CodigoL` varchar(30) NOT NULL,
  `FechaI` varchar(30) NOT NULL,
  `FechaF` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `matricula` int(9) NOT NULL,
  `contraseña` varchar(8) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `carrera` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`matricula`, `contraseña`, `nombre`, `apellidos`, `carrera`, `correo`) VALUES
(181803075, '12345678', 'Martha', 'Soto Luna', 'TI', 'martha@gmail.com'),
(181803076, '12346565', 'Sofia', 'Sanchez Leon ', 'Sistemas', 'daniela@gmail.com'),
(181803074, '12345678', 'Jimena', 'Leon Garcia', 'TI', 'jimena@gmail');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acervo`
--
ALTER TABLE `acervo`
  ADD PRIMARY KEY (`codigoA`);

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`idP`);

--
-- Indices de la tabla `renovar`
--
ALTER TABLE `renovar`
  ADD PRIMARY KEY (`IDR`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `idP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `renovar`
--
ALTER TABLE `renovar`
  MODIFY `IDR` int(30) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
